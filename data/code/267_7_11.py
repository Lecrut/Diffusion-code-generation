def is_long_word(word, min_length=10):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    return len(word) > min_length

if __name__ == '__main__':
    print(is_long_word("short"))
    try:
        print(is_long_word("this is too long"))
    except TypeError as e:
        print(e)