def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "racecar",
        "hello",
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?"
    ]
    for sample in samples:
        print(is_palindrome(sample))