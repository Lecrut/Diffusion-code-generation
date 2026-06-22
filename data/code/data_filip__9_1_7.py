def clean_strings(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    sample = ["  hello  ", " world ", "  python  ", "  123  "]
    cleaned = clean_strings(sample)
    print(cleaned)