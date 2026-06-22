def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    sample_strings = ["radar", "hello", "level", "world", "madam"]
    for string in sample_strings:
        print(f"'{string}' is a palindrome: {is_palindrome(string)}")