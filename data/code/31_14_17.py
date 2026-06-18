def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "race car",
        "Hello World!",
        "Not a palindrome"
    ]

    for sample in samples:
        print(f"'{sample}': {is_palindrome(sample)}")