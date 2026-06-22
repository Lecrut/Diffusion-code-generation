def get_first_word(text):
    if not text.strip():
        return ""
    words = text.split()
    return words[0]

if __name__ == '__main__':
    print(get_first_word("Hello world"))
    print(get_first_word("   leading spaces and multiple words"))
    print(get_first_word(""))
    print(get_first_word("singleword"))
    print(get_first_word("  "))