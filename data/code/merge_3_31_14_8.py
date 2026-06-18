def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "racecar",
        "hello world"
    ]
    
    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")