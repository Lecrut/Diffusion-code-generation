def is_palindrome(s):
    import re
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?"
    ]
    
    for case in test_cases:
        print(f"'{case}' -> {is_palindrome(case)}")