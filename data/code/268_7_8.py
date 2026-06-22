def first_word(sentence):
    import re
    words = re.findall(r'\b\w+\b', sentence)
    return words[0] if words else ''

if __name__ == '__main__':
    print(first_word("  Hello, world!  "))
    print(first_word("This is a test."))
    print(first_word("   Leading and trailing spaces    "))
    print(first_word(""))