def count_digits(s): return len([c for c in s if c.isdigit()])

if __name__ == '__main__':
    sample_string = "abc123xyz789"
    print(count_digits(sample_string))