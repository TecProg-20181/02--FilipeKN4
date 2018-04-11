import random
import string

#WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open("words.txt", 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."

    return getRandomWord(wordlist)

def getRandomWord(wordlist):
    randomWord = random.choice(wordlist)
    #print randomWord
    while getNumberOfDifferentLetters(randomWord) > 8:
        randomWord = random.choice(wordlist)
        #print 'Word changed'

    return randomWord.lower()

def isWordGuessed(secretWord, lettersGuessed):
#    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord(secretWord, lettersGuessed, letter):
     lettersGuessed.append(letter)
     guessed = ''
     for letter in secretWord:
         if letter in lettersGuessed:
             guessed += letter
         else:
             guessed += '_ '

     return guessed

def getNumberOfDifferentLetters(secretWord):
    letters = []
    lettersNumber = 0

    for letter in secretWord:
        if letter in letters:
            pass
        else:
            letters += letter
            lettersNumber+=1

    return lettersNumber

def makeChoice(lettersNumber):


    print '0 continue game'
    print 'Press any key to show the number of different letters in the word'
    option = raw_input('your choice: ')

    if option == '0':
        print '------------'
    else:
        print 'The number of different letters in the word is', lettersNumber
        print '------------'

def getAvailableLetters(lettersGuessed):
    #import string
    # 'abcdefghijklmnopqrstuvwxyz'
    avaliable = string.ascii_lowercase
    for letter in avaliable:
        if letter in lettersGuessed:
            avaliable = avaliable.replace(letter, '')

    return avaliable

def endGame(secretWord, lettersGuessed):
    gameWon = isWordGuessed(secretWord, lettersGuessed) == True
    if gameWon:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


def hangman():

    secretWord = loadWords()
    #print secretWord
    guesses = 8
    lettersGuessed = []
    lettersNumber = getNumberOfDifferentLetters(secretWord)
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'
    makeChoice(lettersNumber)

    while isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        avaliableLetters = getAvailableLetters(lettersGuessed)

        print 'Available letters', avaliableLetters
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:
            print 'Oops! You have already guessed that letter: ', guessed

        elif letter in secretWord:
            guessed = getGuessedWord(secretWord, lettersGuessed, letter)
            print 'Good Guess: ', guessed

        else:
            guesses -=1
            guessed = getGuessedWord(secretWord, lettersGuessed, letter)
            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        endGame(secretWord, lettersGuessed)

hangman()
