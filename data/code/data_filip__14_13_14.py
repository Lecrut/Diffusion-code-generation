def are_characters_distinct(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for count in char_count.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    test_string = "abcdef"
    result = are_characters_distinct(test_string)
    print(result)
    test_string_2 = "hello"
    result_2 = are_characters_distinct(test_string_2)
    print(result_2)