def is_palindrome(text: str) -> bool:
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
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
    for sample in sample_values:
        result = is_palindrome(sample)
        print(result)