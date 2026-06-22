def extract_digits_from_string(mixed_string):
    result = []
    for char in mixed_string:
        if 48 <= ord(char) <= 57:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_data = "Order: 99 items, Total: $150.05, Customer ID: X7Y2Z"
    extracted_digits = extract_digits_from_string(sample_data)
    print(extracted_digits)