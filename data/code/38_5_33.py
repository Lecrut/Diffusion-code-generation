def find_duplicate_characters(s):
    char_count = {}
    duplicates = set()
    
    for char in s:
        if char in char_count:
            duplicates.add(char)
        else:
            char_count[char] = 1
    
    return list(duplicates)

if __name__ == '__main__':
    sample_string = "programming"
    result = find_duplicate_characters(sample_string)
    print(result)