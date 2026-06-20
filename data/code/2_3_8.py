def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    samples = ["racecar", "hello", "madam", "python", "a", "abba"]
    for sample in samples:
        print(is_palindrome(sample))