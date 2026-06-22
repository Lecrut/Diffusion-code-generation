def find_duplicates(s):
    seen = {}
    duplicates = set()
    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    for char, count in seen.items():
        if count > 1:
            duplicates.add(char)
    return list(duplicates)

if __name__ == '__main__':
    test_string1 = "programming"
    result1 = find_duplicates(test_string1)
    print(f"String: {test_string1}, Duplicates: {result1}")
    
    test_string2 = "hello world"
    result2 = find_duplicates(test_string2)
    print(f"String: {test_string2}, Duplicates: {result2}")
    
    test_string3 = "abcdefg"
    result3 = find_duplicates(test_string3)
    print(f"String: {test_string3}, Duplicates: {result3}")