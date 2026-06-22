def has_unique_characters(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    test_string_1 = "abcdefg"
    test_string_2 = "programming"
    result_1 = has_unique_characters(test_string_1)
    result_2 = has_unique_characters(test_string_2)
    print(result_1)
    print(result_2)