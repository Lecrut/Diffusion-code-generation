def is_palindrome(s: str) -> bool:
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = ["RaceCar", "Hello", "A man a plan a canal Panama", "No 'x' in Nixon", "Python"]
    for text in test_cases:
        print(is_palindrome(text))