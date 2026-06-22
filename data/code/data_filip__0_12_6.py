def extract_digits(input_string: str) -> str:
    result = []
    for char in input_string:
        if char.isdigit():
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_data = "Hello123! World@45# 678"
    extracted_digits = extract_digits(sample_data)
    print(extracted_digits)