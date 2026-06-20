def extract_numeric_string(input_string):
    return "".join([char for char in input_string if char.isdigit()])

if __name__ == '__main__':
    result = extract_numeric_string("a1b2c3d4e5f6g7h8i9j0")
    print(result)