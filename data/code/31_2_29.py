def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ["radar", "hello", "level", "world"]
    for value in sample_values:
        result = is_palindrome(value)
        print(f"'{value}' is a palindrome: {result}")