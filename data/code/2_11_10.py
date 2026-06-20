def is_palindrome(text: str) -> bool:
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "racecar",
        "hello",
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "12321",
        "Python"
    ]
    for sample in samples:
        result = is_palindrome(sample)
        print(result)