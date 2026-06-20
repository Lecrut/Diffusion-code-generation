def is_palindrome(s):
    s = s.lower()
    length = len(s)
    half = length // 2
    for i in range(half):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    samples = ["racecar", "hello", "A man a plan a canal Panama", "Was it a car or a cat I saw", "Python"]
    for sample in samples:
        print(is_palindrome(sample))