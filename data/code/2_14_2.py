def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    samples = ["racecar", "hello", "madam", "python", "a", "ab"]
    for sample in samples:
        print(is_palindrome(sample))