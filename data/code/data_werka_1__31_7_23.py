def is_palindrome(s: str) -> bool:
    return s == s[::-1]
if __name__ == '__main__':
    sample_values = ['racecar', 'hello', 'madam', 'world', 'level']
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")