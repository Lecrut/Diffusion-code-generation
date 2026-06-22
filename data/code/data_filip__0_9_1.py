def extract_digits(mixed_string: str) -> str:
    return "".join((char for char in mixed_string if char.isdigit()))

if __name__ == '__main__':
    sample_text = "Order 1234 items on shelf 5B by 2024."
    result = extract_digits(sample_text)
    print(result)