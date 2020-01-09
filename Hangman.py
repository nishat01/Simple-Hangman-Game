
import random

WORDS_FILE = "words.txt"

def getWords():
    print("Loading word list from file...")
    data = open(WORDS_FILE, 'r')
    line = data.readline()
    wlist = line.split()
    print("  ", len(wlist), "wWrds loaded.")
    return wlist

def pickWord(wordlist):
    return random.choice(wordlist)

# ----------------------------------------------------------------------------------
wordlist = getWords()

def isWordGuessed(word, letters):
    # word: to be guessed
    # letters: guessed by the player so far
    # returns: True if all the letters of word are in letters; False otherwise
    
    c = 0
    for i in letters:
        if i in word:
            c += 1
    if c == len(word):
        return True
    else:
        return False

def getGuessedWord(word, letters):
    s = []
    for i in word:
        if i in letters:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans

def getAvailableLetters(letters):
    #returns a string comprised of letters in word that 
    #have not yet been guessed.
    
    import string
    ans = list(string.ascii_lowercase)
    for i in letters:
        ans.remove(i)
    return ''.join(ans)

def hangman(word):
    '''
    Starts an interactive game of Hangman.

    - At the start of the game, let the user know how many 
      letters the secret Word contains.
    - Ask the user to input one guess (i.e. letter) per round.
    - The user should receive feedback immediately after each guess 
      whether their guess exists in the secret word.
    - Each player gets 8 chances to make a guess.
    - After each round, the partially guessed word will be displayed, 
        as well as letters that the user has not guessed yet
    '''
    print("Welcome to the game!")
    print("I am thinking of a word that is",len(word),"letters long.")
    
    global letters
    wrongGuess = 0
    letters = []
    
    while 8 - wrongGuess > 0:
        
        if isWordGuessed(word, letters):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            print("You have", 8 - wrongGuess, "guesses left.")
            print("Available letters:", getAvailableLetters(letters))
            guess = str(input("Please guess a letter: ")).lower()
            
            if guess in letters:
                print("Oops! You've already guessed this character:", getGuessedWord(word,letters))
                
            elif guess in word and guess not in letters:
                letters.append(guess)
                print("Good choice:",getGuessedWord(word,letters))
                
            else:
                letters.append(guess)
                wrongGuess += 1
                print("Oops! That letter is not in my word:",getGuessedWord(word,letters))
                
        if 8 - wrongGuess == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was ", word)
            break
        
        else:
            continue
# ----------------------------------------------------------------------------------

word = pickWord(wordlist).lower()
hangman(word)
