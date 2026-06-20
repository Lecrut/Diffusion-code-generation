def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = ['racecar', 'hello', 'A man a plan a canal Panama', 'No lemon, no melon', 'Python']
    for case in test_cases:
        result = is_palindrome(case)
        print(result)