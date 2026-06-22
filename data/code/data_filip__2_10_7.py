def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    samples = ["racecar", "hello", "A man a plan a canal Panama".replace(" ", "").lower(), "", "a", "ab"]
    for sample in samples:
        print(is_palindrome(sample))