def is_palindrome(s: str) -> bool:
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_strings = ["Racecar", "A man, a plan, a canal: Panama", "Hello", "Madam"]
    results = []
    for text in test_strings:
        results.append((text, is_palindrome(text)))
    for string, is_pal in results:
        print(f"{string}: {is_pal}")