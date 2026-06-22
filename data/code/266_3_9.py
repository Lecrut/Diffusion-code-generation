MAX_WORD_LENGTH = 0
LONGEST_WORD = ""

def find_longest_word(words):
    global MAX_WORD_LENGTH, LONGEST_WORD
    for word in words:
        if len(word) > MAX_WORD_LENGTH:
            MAX_WORD_LENGTH = len(word)
            LONGEST_WORD = word

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    find_longest_word(sample_words)
    print(f"Longest word: {LONGEST_WORD}, Length: {MAX_WORD_LENGTH}")