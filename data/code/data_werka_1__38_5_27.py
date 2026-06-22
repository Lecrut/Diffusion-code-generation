def find_duplicates(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
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
    
    test_string3 = "abcdefg"
    result3 = find_duplicates(test_string3)
    print(f"Input: {test_string3}")
    print(f"Duplicates: {result3}")