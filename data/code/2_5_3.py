def is_palindrome(text: str) -> bool:
    normalized = text.lower()
    left = 0
    right = len(normalized) - 1
    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_cases = ["Racecar", "Hello", "Noon", "Was it a car or a cat I saw", "Python"]
    for sample in test_cases:
        print(f"{sample}: {is_palindrome(sample)}")