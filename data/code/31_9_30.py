def is_palindrome(s):
    return s.lower() == s[::-1].lower()

if __name__ == '__main__':
    sample_strings = ["racecar", "hello", "A man a plan a canal Panama"]
    for string in sample_strings:
        print(f"'{string}' is a palindrome: {is_palindrome(string)}")