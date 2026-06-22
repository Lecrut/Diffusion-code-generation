def is_palindrome(text: str) -> bool:
    cleaned = ''.join((char.lower() for char in text if char.isalnum()))
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    test_cases = ['racecar', 'hello', 'A man, a plan, a canal: Panama', 'No lemon, no melon', 'Palindrome', 'Python', '12321', '12345', '', 'a', 'AbBa', 'Was it a car or a cat I saw?']
    for test in test_cases:
        result = is_palindrome(test)
        print(f"Input: '{test}' => Is Palindrome: {result}")