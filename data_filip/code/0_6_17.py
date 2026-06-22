def extract_and_count_digits(text: str) -> int:
    digit_characters = [c for c in text if c.isdecimal()]
    return len(digit_characters)

if __name__ == '__main__':
    sample_string = "Python3.9isGreat!2024"
    result = extract_and_count_digits(sample_string)
    print(result)