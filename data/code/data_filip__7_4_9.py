def locate_first_special_character(input_text: str) -> str | None:
    ascii_letters_and_digits = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    index = 0
    length = len(input_text)
    while index < length:
        current_char = input_text[index]
        index += 1
        if current_char not in ascii_letters_and_digits:
            if not current_char.isspace():
                return current_char
    return None

if __name__ == '__main__':
    print(locate_first_special_character("valid text without symbols"))
    print(locate_first_special_character("valid text@with symbol"))
    print(locate_first_special_character("123456789"))
    print(locate_first_special_character(""))
    print(locate_first_special_character("   spaces   "))