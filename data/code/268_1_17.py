def get_first_word(text):
    words = text.split()
    return words[0] if words else ""

if __name__ == '__main__':
    print(get_first_word("Hello world"))
    print(get_first_word("   leading spaces and multiple words"))
    print(get_first_word(""))
    print(get_first_word("singleword"))