def is_palindrome(s):
    cleaned = s.lower()
    cleaned = cleaned.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "")
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    sample1 = "RaceCar"
    sample2 = "Hello"
    sample3 = "A man, a plan, a canal: Panama"
    print(is_palindrome(sample1))
    print(is_palindrome(sample2))
    print(is_palindrome(sample3))