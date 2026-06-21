def find_repeated_characters(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return ''.join(sorted(duplicates))

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_characters(sample_string)
    print(result)