def contains_all_unique_characters(s):
    if len(s) == 0:
        return True
    seen_characters = set()
    for char in s:
        if char in seen_characters:
            return False
        seen_characters.add(char)
    return True

if __name__ == '__main__':
    test_string = "abcdefg123"
    result = contains_all_unique_characters(test_string)
    print(result)