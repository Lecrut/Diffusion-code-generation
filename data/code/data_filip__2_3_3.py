def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ["racecar", "hello", "madam", "python", "a"]
    for value in sample_values:
        print(f"is_palindrome('{value}') = {is_palindrome(value)}")