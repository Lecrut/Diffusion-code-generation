def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = ['Racecar', 'Hello', 'A man a plan a canal Panama', 'Was it a car or a cat I saw', 'Python']
    for case in test_cases:
        print(is_palindrome(case))