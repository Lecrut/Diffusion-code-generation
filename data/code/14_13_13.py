def all_distinct(s):
    seen = {}
    for char in s:
        if char in seen:
            return False
        seen[char] = True
    return True

if __name__ == '__main__':
    test_cases = ["abcde", "aabbcc", "hello", "world", ""]
    for case in test_cases:
        print(all_distinct(case))