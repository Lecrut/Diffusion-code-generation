def are_all_characters_unique(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string = "abcdef"
    result = are_all_characters_unique(test_string)
    print(result)