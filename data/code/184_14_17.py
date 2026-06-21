def contains_token(text: str, token: str) -> bool:
    words = text.split()
    return any(word == token for word in words)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_token = "fox"
    result = contains_token(sample_text, target_token)
    print(f"Token '{target_token}' found: {result}")