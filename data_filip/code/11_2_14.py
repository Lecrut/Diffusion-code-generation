def extract_repeated_characters(s):
    all_chars = set(s)
    unique_chars = set()
    repeated_chars = set()
    for char in s:
        if char in unique_chars:
            repeated_chars.add(char)
        else:
            unique_chars.add(char)
    return sorted(list(repeated_chars))

if __name__ == '__main__':
    sample_string = "hello world"
    result = extract_repeated_characters(sample_string)
    print(result)