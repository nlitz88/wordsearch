import random, math, string


def randomWordsFromFile(file, quant):
    
    # read words from text file
    wordsfile = open(file, "r")
    
    wordListLength = 0
    wordList = []

    # determine length of list and add words to list object
    for word in wordsfile:
        wordListLength += 1
        wordList.append(word)

    if quant > wordListLength:
        return "Out of range (length = " + str(wordListLength) + ")"

    else:
        # define list where radomly selected words will be stored
        workingWordList = []

        for w in range(0, quant):
            wordIndex = random.randrange(0, len(wordList))

            word = wordList[wordIndex]
            wordList.remove(word)

            word = word.strip("\n")
            workingWordList.append(word)
        
        return workingWordList


# generates blank matrix for words to be plotted in
def generateMatrix(rows, cols):

    matrix = []

    for r in range(0, rows):
        matrix.append([])
        for c in range(0, cols):
            matrix[r].append(0)
    
    return matrix


# checks individual coordinates to see if a letter of a word can be placed there
def checkCoords(matrix, rowIndex, colIndex, word, x):

    if rowIndex < 1 or colIndex < 1:
        return False

    # Alternate method: Check to see if rowIndex OR colIndex are out of bounds
    elif (rowIndex > len(matrix) - 1) or (colIndex > len(matrix[0]) - 1):
        return False

    # If neither of those conditions return false, then evaluate value at provided position
    if matrix[rowIndex][colIndex] == 0 or matrix[rowIndex][colIndex] == word[x]:
        return True
    else:
        return False


def randomDirection(plottableDirections):
    x = random.randrange(0, len(plottableDirections))
    return plottableDirections[x]


# checks if word can fit in 
def canPlot(word, matrix, rowIndex, colIndex, direction):

    word = list(word)

    # determine if in a given direction, enough space for word to fit (does it stay in range of matrix?)
    if direction == 0:
        
        for x in range(0, len(word)):
            print("checking at " + str(((rowIndex), (colIndex + x))))
            if checkCoords(matrix, rowIndex, (colIndex + x), word, x):
                continue
            else:
                return False
        return True
    
    # repeat for each different direction
    elif direction == 45:

        for x in range(0, len(word)):
            print("checking at " + str(((rowIndex - x), (colIndex + x))))
            if checkCoords(matrix, (rowIndex - x), (colIndex + x), word, x):
                continue
            else:
                return False
        return True

    elif direction == 90:

        for x in range(0, len(word)):
            print("checking at " + str(((rowIndex - x), (colIndex))))
            if checkCoords(matrix, (rowIndex - x), colIndex, word, x):
                continue
            else:
                return False
        return True
    
    elif direction == 135:

        for x in range(0, len(word)):
            print("checking at " + str(((rowIndex - x), (colIndex - x))))
            if checkCoords(matrix, (rowIndex - x), (colIndex - x), word, x):
                continue
            else:
                return False
        return True
    
    elif direction == 180:

        for x in range(0, len(word)):
            print("checking at " + str(((rowIndex), (colIndex - x))))
            if checkCoords(matrix, rowIndex, (colIndex - x), word, x):
                continue
            else:
                return False
        return True

    elif direction == 225:
        
        for x in range(0, len(word)):
            print("checking at " + str(((rowIndex + x), (colIndex - x))))
            if checkCoords(matrix, (rowIndex + x), (colIndex - x), word, x):
                continue
            else:
                return False
        return True

    elif direction == 270:

        for x in range(0, len(word)):
            print("checking at " + str(((rowIndex + x), (colIndex))))
            if checkCoords(matrix, (rowIndex + x), colIndex, word, x):
                continue
            else:
                return False
        return True
    
    elif direction == 315:

        for x in range(0, len(word)):
            print("checking at " + str(((rowIndex + x), (colIndex + x))))
            if checkCoords(matrix, (rowIndex + x), (colIndex + x), word, x):
                continue
            else:
                return False
        return True


def plotWords(words, matrix):

    # possible angles from any given coordinates
    angles = [0, 45, 90, 135, 180, 225, 270, 315]
    plottableAngles = []

    # for every workable word, assign a direction, see if it's plottable in that direction at that index
    # if not, change direction
    # if still not valid, change row/col indices

    # DOESN'T ACCOUNT FOR IMPOSSIBLE WORDS: POTENTIALLY TRY TO FIX THAT
    print(words)

    for word in words:

        plottable = False
        while not plottable:
            
            plottableAngles = []
            # get random row index
            rowIndex = random.randrange(len(matrix))
            colIndex = random.randrange(len(matrix[0]))

            print("Coords: " + str((rowIndex, colIndex)))
         
            for potentialAngle in angles:
                if canPlot(word, matrix, rowIndex, colIndex, potentialAngle):
                    plottableAngles.append(potentialAngle)
                    print("plottable at angle " + str(potentialAngle))
                    plottable = True
                else:
                    print("not plottable at angle " + str(potentialAngle))
            
        # randomly pick which of the potential angles to plot at
        direction = randomDirection(plottableAngles)

        # make word series of characters in list
        word = list(word)


        # plot word in whatever direction
        if direction == 0:
            for x in range(0, len(word)):
                print(word[x] + " at " + str((rowIndex , (colIndex + x))))
                matrix[rowIndex][colIndex + x] = word[x]
        
        elif direction == 45:
            print("45 degrees chosen")
            for x in range(0, len(word)):
                print(word[x] + " at " + str(((rowIndex - x), (colIndex + x))))
                matrix[rowIndex - x][colIndex + x] = word[x]

        elif direction == 90:
            print("90 degrees chosen")
            for x in range(0, len(word)):
                print(word[x] + " at " + str(((rowIndex - x), colIndex)))
                matrix[rowIndex - x][colIndex] = word[x]
        
        elif direction == 135:
            print("135 degrees chosen")
            for x in range(0, len(word)):
                print(word[x] + " at " + str(((rowIndex - x), (colIndex - x))))
                matrix[rowIndex - x][colIndex - x] = word[x]
        
        elif direction == 180:
            print("180 degrees chosen")
            for x in range(0, len(word)):
                print(word[x] + " at " + str((rowIndex , (colIndex + x))))
                matrix[rowIndex][colIndex - x] = word[x]

        elif direction == 225:
            print("225 degrees chosen")
            for x in range(0, len(word)):
                print(word[x] + " at " + str(((rowIndex + x), (colIndex - x))))
                matrix[rowIndex + x][colIndex - x] = word[x]

        
        elif direction == 270:
            print("270 degrees chosen")
            for x in range(0, len(word)):
                print(word[x] + " at " + str(((rowIndex + x), colIndex)))
                matrix[rowIndex + x][colIndex] = word[x]
        
        elif direction == 315:
            print("45 degrees chosen")
            for x in range(0, len(word)):
                print(word[x] + " at " + str(((rowIndex + x), (colIndex + x))))
                matrix[rowIndex + x][colIndex + x] = word[x]
    
    return matrix


# replace all unoccupied spaces with random letter
def replaceBlanks(matrix):

    alphabet = string.ascii_lowercase
    alphaList = list(alphabet)

    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[r])):

            if matrix[c][r] == 0:
                charIndex = random.randrange(0, len(alphaList))
                matrix[c][r] = alphaList[charIndex]

    
    return matrix



# print out matrix
matrix = generateMatrix(15,15)
for index, row in enumerate(matrix):
    print(index,row)


# generate words from word list
words = randomWordsFromFile("words.txt", 10)


# print out matrix generatued by plotwords function
for index, row in enumerate(plotWords(words, matrix)):
    print(index, row)
print(words)


# print final word search
for index, row in enumerate(replaceBlanks(matrix)):
    print(index, row)
print(words)


# Implement system where if all possible indices for a word have been tried, regenerate words and try again
# or try to only find new random word that will fit
# or also make function to share a letter with another word allowing it to fit

# Try each indice until all have been tried (use hash table?)
# if that doesn't work, replot all words
# Keep track of every index that a word has been at previously to figure out each possible combination??
# Should be some mathematical way of calculating optimal configuration

# next time, add sys, import and make program accept args



# function during plotting that randomly decides if the next word will overlap with a word that is already plotted,
# then, it will check if it can overlap with that word at any given possible index.