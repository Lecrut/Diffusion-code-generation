def count_digits(s): return len([c for c in s if c.isdigit()])

if __name__ == '__main__':
    print(count_digits("abc123def456"))