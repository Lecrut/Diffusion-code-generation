LONG_WORD_THRESHOLD = 10

def is_long_word(word):
    return len(word) > LONG_WORD_THRESHOLD

if __name__ == '__main__':
    print(is_long_word("short"))
    print(is_long_word("thisiswaylong"))
    print(is_long_word("exactlytwelve"))