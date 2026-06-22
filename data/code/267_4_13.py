def is_long_word(word):
    return len(word) > 8

if __name__ == '__main__':
    print(is_long_word("short"))
    print(is_long_word("thisiswaylong"))
    print(is_long_word("exactlynine"))