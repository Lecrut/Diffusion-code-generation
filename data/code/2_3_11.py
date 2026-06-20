def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ["radar", "hello", "A man a plan a canal Panama".replace(" ", "").lower(), "12321", "12345"]
    for value in sample_values:
        print(is_palindrome(value))