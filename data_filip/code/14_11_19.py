def has_unique_chars(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_cases = ["abcde", "hello", "", "a", "abcc"]
    for tc in test_cases:
        print(has_unique_chars(tc))