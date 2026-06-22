def extract_digits(s):
    result = []
    for char in s:
        if char.isdigit():
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    input_string = "a1b2c3d4e5f6g7h8i9j0"
    output = extract_digits(input_string)
    print(output)