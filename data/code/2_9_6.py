def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    sample_input = "racecar"
    print(is_palindrome(sample_input))