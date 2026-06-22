def is_palindrome(text):
    return text == text[::-1]

if __name__ == '__main__':
    test_strings = ["radar", "hello", "level", "python"]
    for s in test_strings:
        print(is_palindrome(s))