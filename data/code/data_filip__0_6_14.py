def count_digits(s: str) -> int:
    digits = [char for char in s if char in "0123456789"]
    return len(digits)

if __name__ == '__main__':
    test_string = "Hello 2024 World 3.14"
    print(count_digits(test_string))