def is_palindrome(text):
    return text == text[::-1]

if __name__ == '__main__':
    sample_strings = ["racecar", "hello", "madam", "world", "noon"]
    for s in sample_strings:
        print(is_palindrome(s))