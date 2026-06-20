def count_digits(s: str) -> int:
    digits = [c for c in s if c.isdigit()]
    return len(digits)

if __name__ == '__main__':
    test_strings = ["Hello123", "NoDigitsHere", "999", "Mixed55Test"]
    for text in test_strings:
        print(count_digits(text))