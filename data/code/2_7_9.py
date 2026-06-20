def check_palindrome_symmetry(s):
    return all(a == b for a, b in zip(s, reversed(s)))

if __name__ == '__main__':
    test_cases = ["racecar", "hello", "madam", "world", "12321"]
    for case in test_cases:
        print(f"{case}: {check_palindrome_symmetry(case)}")