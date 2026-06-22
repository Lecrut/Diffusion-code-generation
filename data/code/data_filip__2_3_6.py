def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    samples = ["racecar", "hello", "madam", "python", "level"]
    for sample in samples:
        print(is_palindrome(sample))