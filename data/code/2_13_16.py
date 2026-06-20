def is_palindrome(s: str) -> bool:
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "Was it a car or a cat I saw?"]
    results = []
    for s in sample_strings:
        results.append(is_palindrome(s))
    print(results)