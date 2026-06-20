def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "No lemon, no melon",
        "Was it a car or a cat I saw?",
        "Python"
    ]
    for sample in samples:
        print(is_palindrome(sample))