def is_word_long(word):
    return len(word) > 7

if __name__ == '__main__':
    print(is_word_long("example"))
    print(is_word_long("hi"))