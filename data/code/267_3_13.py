def is_word_long(word):
    MIN_LENGTH = 6
    if not isinstance(word, str) or word == "":
        raise ValueError("Input must be a non-empty string")
    return len(word) > MIN_LENGTH

if __name__ == '__main__':
    print(is_word_long("example"))
    print(is_word_long("hi"))