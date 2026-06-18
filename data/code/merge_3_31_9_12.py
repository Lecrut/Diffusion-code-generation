def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    sample_strings = ["racecar", "hello", "_", "!x!"]
    for text in sample_strings:
        result = is_palindrome(text)
        print(f"'{text}'" + (" IS a palindrome." if result else " is NOT a palindrome."))