def find_duplicate_characters(s):
    char_count = {}
    duplicates = set()
    for char in s:
        if char.isalpha():
            count = char_count.get(char.lower(), 0) + 1
            char_count[char.lower()] = count
            if count == 2:
                duplicates.add(char.lower())
    return list(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_characters(sample_string)
    print(result)