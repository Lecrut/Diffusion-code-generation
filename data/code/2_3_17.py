def is_palindrome(text):
    return text == text[::-1]

if __name__ == '__main__':
    sample1 = "racecar"
    sample2 = "hello"
    result1 = is_palindrome(sample1)
    result2 = is_palindrome(sample2)
    print(result1)
    print(result2)