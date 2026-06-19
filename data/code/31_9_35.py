def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_strings = ["racecar", "hello", "level", "world"]
    for string in sample_strings:
        print(f"'{string}' is a palindrome: {is_palindrome(string)}")