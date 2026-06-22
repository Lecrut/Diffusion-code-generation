def extract_repeated_chars(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return sorted(repeated)

if __name__ == '__main__':
    sample = "hello world programming"
    result = extract_repeated_chars(sample)
    print(result)