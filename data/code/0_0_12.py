def extract_digits_as_integer(text):
    digits = ''.join(char for char in text if char.isdigit())
    if not digits:
        return 0
    return int(digits)

if __name__ == '__main__':
    print(extract_digits_as_integer("abc123def456"))
    print(extract_digits_as_integer("no_digits_here"))
    print(extract_digits_as_integer("789"))
    print(extract_digits_as_integer(""))
    print(extract_digits_as_integer("a1b2c3"))