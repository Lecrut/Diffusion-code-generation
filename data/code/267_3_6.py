WORD_LENGTH_THRESHOLD = 6

def is_word_long(word):
    return len(word) > WORD_LENGTH_THRESHOLD

if __name__ == '__main__':
    print(is_word_long("example"))
    print(is_word_long("hi"))