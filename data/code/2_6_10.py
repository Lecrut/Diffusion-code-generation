def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    samples = ["racecar", "hello", "a", "ab", "madam", "python"]
    results = []
    for sample in samples:
        results.append(is_palindrome(sample))
    print(results)