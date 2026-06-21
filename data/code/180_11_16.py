TARGET_WORD = "target"
LARGE_TEXT = "this is a very long string designed to test the efficiency of substring searching in Python for very long texts"

def check_word_presence(text, word):
    words_set = set(text.split())
    return word in words_set

if __name__ == '__main__':
    result = check_word_presence(LARGE_TEXT, TARGET_WORD)
    print(result)