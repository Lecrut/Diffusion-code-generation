def extract_repeated_chars(text):
    seen = set()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return sorted(list(repeated))

if __name__ == '__main__':
    sample_string = "programming"
    result = extract_repeated_chars(sample_string)
    print(result)