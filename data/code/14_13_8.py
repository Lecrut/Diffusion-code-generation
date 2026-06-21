def all_distinct(s):
    seen = {}
    for char in s:
        if char in seen:
            return False
        seen[char] = True
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    print(all_distinct(test_string_1))
    print(all_distinct(test_string_2))