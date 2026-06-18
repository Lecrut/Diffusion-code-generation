import re

def is_palindrome(s: str) -> bool:
    return s == ''.join(reversed(list(filter(str.isalnum, s)))) if isinstance(s, str) else False

if __name__ == '__main__':
    test_cases = [["racecar", True], ["A man a plan a canal Panama", True], ["hello world", False]]
    for case in test_cases:
        print(f"{case[0]} is palindrome: {is_palindrome(case[0].lower())}")