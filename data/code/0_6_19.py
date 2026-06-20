def extract_digit_count(s): return len([c for c in s if c.isdigit()])
if __name__ == '__main__':
    print(extract_digit_count('abc123xyz456'))