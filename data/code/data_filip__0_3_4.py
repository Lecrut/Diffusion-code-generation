def extract_digits(input_string: str) -> str:
    return "".join(char for char in input_string if char.isdigit())

if __name__ == '__main__':
    sample_string = "a1b2c3d4"
    result = extract_digits(sample_string)
    print(result)