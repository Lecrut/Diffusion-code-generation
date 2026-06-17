def find_duplicate_chars(text):
    char_count = {}
    duplicates = []
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 0
        count = char_count.get(char, 0) + 1
        char_count[char] = count
    seen_duplicates = set()
    for char, count in char_count.items():
        if count > 1 and char not in seen_duplicates:
            duplicates.append(char)
            seen_duplicates.add(char)
    return list(set(duplicates))
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_chars(sample_string)
    print(result)