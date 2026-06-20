def extract_digits_to_integer(s: str) -> int:
    digits = [char for char in s if char.isdigit()]
    if not digits:
        return 0
    return int("".join(digits))

if __name__ == "__main__":
    sample_strings = ["abc123xyz", "no_digits_here", "0042", "!@#5678", ""]
    for text in sample_strings:
        result = extract_digits_to_integer(text)
        print(f"Input: '{text}' -> Output: {result}")