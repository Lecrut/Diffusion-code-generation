def find_duplicates(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    duplicates = []
    seen_chars = set()
    for char, count in char_count.items():
        if count > 1 and char not in seen_chars:
            duplicates.append(char)
            seen_chars.add(char)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)