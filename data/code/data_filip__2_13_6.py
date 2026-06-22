def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    samples = ["racecar", "hello", "A man a plan a canal Panama".replace(" ", "").lower(), "madam", "python"]
    for sample in samples:
        cleaned = sample.replace(" ", "").lower()
        print(is_palindrome(cleaned))