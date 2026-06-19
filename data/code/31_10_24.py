def is_palindrome(s: str) -> bool:
    import re
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?"
    ]
    
    for value in sample_values:
        print(is_palindrome(value))