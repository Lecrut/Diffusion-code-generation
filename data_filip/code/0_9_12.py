def extract_digits(mixed_string: str) -> str:
    return "".join(char for char in mixed_string if char.isdigit())

if __name__ == "__main__":
    sample_data = "abc123def456ghi789"
    result = extract_digits(sample_data)
    print(result)