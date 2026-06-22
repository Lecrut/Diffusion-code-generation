def extract_digits(complex_string: str) -> str:
    return "".join(char for char in complex_string if char.isdigit())

if __name__ == '__main__':
    sample_data = "User: A1b@2#C3$D4%5E6&7*8(9)0-!~`|;:',.<>?/"
    result = extract_digits(sample_data)
    print(result)