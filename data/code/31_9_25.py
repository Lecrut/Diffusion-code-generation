def is_palindrome(s):
    return s.lower() == s[::-1].lower()

if __name__ == '__main__':
    sample_values = ["racecar", "hello", "Aibohphobia", "Noon", "Palindrome"]
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")