def all_distinct(s):
    seen = {}
    for char in s:
        if char in seen:
            return False
        seen[char] = True
    return True

if __name__ == '__main__':
    test_cases = ["hello", "world", "python", "abcde", "aabb", ""]
    for case in test_cases:
        result = all_distinct(case)
        print(result)