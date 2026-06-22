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
    samples = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "",
        "a",
        "ab"
    ]
    for sample in samples:
        result = is_palindrome(sample.lower().replace(" ", ""))
        print(result)