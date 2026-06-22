def is_palindrome_symmetric(text):
    return all(a == b for a, b in zip(text, reversed(text)))

if __name__ == '__main__':
    sample1 = "radar"
    sample2 = "hello"
    sample3 = "abba"
    sample4 = "Python"
    result1 = is_palindrome_symmetric(sample1)
    result2 = is_palindrome_symmetric(sample2)
    result3 = is_palindrome_symmetric(sample3)
    result4 = is_palindrome_symmetric(sample4)
    print(result1)
    print(result2)
    print(result3)
    print(result4)