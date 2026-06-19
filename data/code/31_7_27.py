def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ["radar", "hello", "level", "world", "madam"]
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")