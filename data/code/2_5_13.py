def is_palindrome(s: str) -> bool:
    cleaned = ''.join(char for char in s if char.isalnum()).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_strings = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "12321"
    ]
    for s in test_strings:
        result = is_palindrome(s)
        print(result)