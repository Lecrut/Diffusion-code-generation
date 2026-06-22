def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_strings = ["radar", "hello", "A man a plan a canal Panama", "noon"]
    results = [is_palindrome(s) for s in sample_strings]
    for original, result in zip(sample_strings, results):
        print(f"{original}: {result}")