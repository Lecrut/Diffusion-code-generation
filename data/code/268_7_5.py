def first_word(sentence):
    words = sentence.split()
    return words[0] if words else ""

if __name__ == '__main__':
    print(first_word("Hello, world!"))
    print(first_word("   Leading spaces."))
    print(first_word("Trailing spaces.   "))
    print(first_word("  Multiple   spaces.  "))
    print(first_word(""))
    print(first_word("."))