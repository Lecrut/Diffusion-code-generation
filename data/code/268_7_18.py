def find_first_word(sentence):
    words = sentence.split()
    return words[0] if words else ""

if __name__ == '__main__':
    print(find_first_word("Hello, world!"))
    print(find_first_word("   Leading spaces are ignored."))
    print(find_first_word("Trailing spaces    "))
    print(find_first_word(""))