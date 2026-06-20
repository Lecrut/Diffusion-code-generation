def extract_digits_as_integer(text):
    digits = [char for char in text if char.isdigit()]
    if not digits:
        return 0
    return int(''.join(digits))

if __name__ == '__main__':
    result1 = extract_digits_as_integer("abc123def456")
    print(result1)
    result2 = extract_digits_as_integer("no_digits_here")
    print(result2)
    result3 = extract_digits_as_integer("789")
    print(result3)