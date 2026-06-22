def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    samples = ["racecar", "hello", "A man, a plan, a canal: Panama", "No 'x' in Nixon", "not a palindrome", "", "a"]
    for sample in samples:
        print(is_palindrome(sample))