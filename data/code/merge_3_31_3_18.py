import sys

def is_palindrome(s: str) -> bool:
    return s == "".join(reversed(s))

if __name__ == '__main__':
    test_string = "racecar"
    result = is_palindrome(test_string)
    print(result)