def is_palindrome(s: str) -> bool:
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "No lemon, no melon"]
    for test in test_strings:
        result = is_palindrome(test)
        print(result)