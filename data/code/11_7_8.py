def find_repeated_characters(input_string):
    seen = set()
    duplicates = set()
    for char in input_string:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return "".join(sorted(duplicates))

if __name__ == '__main__':
    sample_text = "programming"
    result = find_repeated_characters(sample_text)
    print(result)