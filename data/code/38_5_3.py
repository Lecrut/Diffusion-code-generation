def find_duplicates(s):
    char_counts = {}
    duplicates = set()
    for char in s:
        if char in char_counts:
            if char_counts[char] == 1:
                duplicates.add(char)
        char_counts[char] = char_counts.get(char, 0) + 1
    return list(duplicates)
if __name__ == '__main__':
    test_string1 = "programming"
    result1 = find_duplicates(test_string1)
    print(f"String: {test_string1}, Duplicates: {result1}")
    test_string2 = "aabbccddeeff"
    result2 = find_duplicates(test_string2)
    print(f"String: {test_string2}, Duplicates: {result2}")
    test_string3 = "abcde"
    result3 = find_duplicates(test_string3)
    print(f"String: {test_string3}, Duplicates: {result3}")
    test_string4 = "hello world"
    result4 = find_duplicates(test_string4)
    print(f"String: {test_string4}, Duplicates: {result4}")