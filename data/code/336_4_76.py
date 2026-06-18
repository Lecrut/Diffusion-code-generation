def find_duplicates(s):
    char_count = {}
    duplicates = []
    for char in s:
        if char.isalpha():
            count = char_count.get(char.lower(), 0) + 1
            char_count[char.lower()] = count
            if count == 2 and char not in duplicates:
                duplicates.append(char)
    return sorted(duplicates, key=str.upper)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)