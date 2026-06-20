def count_digits(s: str) -> int:
    return sum(1 for c in s if c.isdigit())

if __name__ == '__main__':
    sample = "abc123def45"
    print(count_digits(sample))