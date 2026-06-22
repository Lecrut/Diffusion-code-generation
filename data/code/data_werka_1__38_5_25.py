def find_duplicates(s):
    char_set = set()
    duplicates = set()
    for char in s:
        if char in char_set:
            duplicates.add(char)
        else:
            char_set.add(char)
    return list(duplicates)

if __name__ == '__main__':
    test_string1 = "programming"
    result1 = find_duplicates(test_string1)
    print(f"Input: {test_string1}")
    print(f"Duplicates: {result1}")

    test_string2 = "hello world"
    result2 = find_duplicates(test_string2)
    print(f"Input: {test_string2}")
    print(f"Duplicates: {result2}")

    test_string3 = "abcde"
    result3 = find_duplicates(test_string3)
    print(f"Input: {test_string3}")
    print(f"Duplicates: {result3}")