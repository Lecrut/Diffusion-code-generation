def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "hello", "A man a plan a canal Panama", "No lemon, no melon", "Python"]
    for case in test_cases:
        print(f"is_palindrome('{case}') = {is_palindrome(case)}")