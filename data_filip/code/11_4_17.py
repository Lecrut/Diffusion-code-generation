def find_duplicate_chars(input_string):
    lower_string = input_string.lower()
    seen = set()
    duplicates = set()
    for char in lower_string:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return list(duplicates)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = find_duplicate_chars(sample_text)
    print(result)