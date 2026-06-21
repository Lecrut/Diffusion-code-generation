def contains_token(text: str, token: str) -> bool:
    return token in text.split()

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_token = "fox"
    result = contains_token(sample_text, target_token)
    print(f"Token Found: {result}")