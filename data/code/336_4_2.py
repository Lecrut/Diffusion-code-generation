def find_duplicates(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    duplicates = []
    seen = set()
    for char, count in sorted(char_count.items()):
        if count > 1 and char not in seen:
            duplicates.append(char)
            seen.add(char)
    return duplicates
if __name__ == '__main__':
    test_string = "hello world"
    result = find_duplicates(test_string)
    print(result)