def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a cat and I? ",
        ""
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")