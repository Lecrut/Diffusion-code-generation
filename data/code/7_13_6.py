def has_non_alphanumeric_non_space(s: str) -> bool:
    for char in s:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    print(has_non_alphanumeric_non_space("Hello World!"))
    print(has_non_alphanumeric_non_space("Hello World"))
    print(has_non_alphanumeric_non_space("123 456"))