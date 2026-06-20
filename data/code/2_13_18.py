def is_palindrome(text: str) -> bool:
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "No 'x' in Nixon"]
    for s in sample_strings:
        result = is_palindrome(s)
        print(result)