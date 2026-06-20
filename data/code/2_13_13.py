def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?",
        "No lemon, no melon",
        "Python"
    ]
    for value in sample_values:
        result = is_palindrome(value)
        print(result)