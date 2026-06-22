def is_palindrome(s: str) -> bool:
    if not s:
        return True
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_cases = ["", "a", "racecar", "hello", "A man, a plan, a canal: Panama", "No 'x' in Nixon"]
    for text in test_cases:
        result = is_palindrome(text)
        print(result)