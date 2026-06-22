def extract_numeric_string(input_str: str) -> str:
    return "".join([char for char in input_str if char.isdigit()])

if __name__ == '__main__':
    sample_input = "abc123def456"
    result = extract_numeric_string(sample_input)
    print(result)