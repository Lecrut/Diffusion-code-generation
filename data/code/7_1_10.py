import string

def contains_special_characters(text: str) -> bool:
    printable_ascii = string.printable
    ascii_letters_digits = string.ascii_letters + string.digits + ' '
    for char in text:
        code_point = ord(char)
        if code_point < 32 or code_point > 126:
            return True
        if char not in ascii_letters_digits:
            return True
    return False

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = contains_special_characters(sample_string)
    print(result)