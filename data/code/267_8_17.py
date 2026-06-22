def is_word_long(word):
    return len(word) > 5

if __name__ == '__main__':
    print(is_word_long("Python"))
    print(is_word_long("Hi"))
    print(is_word_long("HelloWorld"))