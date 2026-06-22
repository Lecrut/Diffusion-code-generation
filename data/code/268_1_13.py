def get_first_word(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    return words[0] if words else ""

if __name__ == '__main__':
    print(get_first_word("Hello world"))
    print(get_first_word("   leading spaces and multiple words"))
    print(get_first_word(""))
    print(get_first_word("singleword"))
    try:
        print(get_first_word(123))
    except ValueError as e:
        print(e)