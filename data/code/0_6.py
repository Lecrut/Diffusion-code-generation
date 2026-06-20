def count_digits(s: str) -> int:
    return sum(1 for c in s if c.isdigit())

if __name__ == '__main__':
    print(count_digits("abc123!@#456"))