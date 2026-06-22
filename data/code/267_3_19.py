def is_word_long(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return len(word) > 7

if __name__ == '__main__':
    print(is_word_long("example"))
    print(is_word_long("hi"))