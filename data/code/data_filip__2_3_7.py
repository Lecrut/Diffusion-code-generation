def is_palindrome(text):
    return text == text[::-1]

if __name__ == '__main__':
    sample1 = "radar"
    sample2 = "hello"
    print(is_palindrome(sample1))
    print(is_palindrome(sample2))