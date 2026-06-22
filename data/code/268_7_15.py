def first_word(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    if not words:
        return ""
    return words[0]

if __name__ == '__main__':
    print(first_word("Hello, world!"))
    print(first_word("   Leading spaces."))
    print(first_word("Trailing spaces.   "))
    print(first_word("Multiple   spaces."))
    print(first_word(""))