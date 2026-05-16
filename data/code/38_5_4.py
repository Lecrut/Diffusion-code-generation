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
    test_string1 = "aabbccddeeff"
    result1 = find_duplicates(test_string1)
    print(f"Input: {test_string1}")
    print(f"Duplicates: {result1}")
    test_string2 = "abcde"
    result2 = find_duplicates(test_string2)
    print(f"Input: {test_string2}")
    print(f"Duplicates: {result2}")
    test_string3 = "hello world"
    result3 = find_duplicates(test_string3)
    print(f"Input: {test_string3}")
    print(f"Duplicates: {result3}")
    test_string4 = "programming"
    result4 = find_duplicates(test_string4)
    print(f"Input: {test_string4}")
    print(f"Duplicates: {result4}")