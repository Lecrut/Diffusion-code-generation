def get_repeated_characters(text):
    seen = set()
    duplicates = set()
    for char in text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return sorted(duplicates)

if __name__ == '__main__':
    sample_string = "programming"
    result = get_repeated_characters(sample_string)
    print(result)