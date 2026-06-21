def check_token_in_string(text: str, target_token: str) -> bool:
    tokens = text.split()
    return target_token in tokens

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_token = "fox"
    result = check_token_in_string(sample_text, target_token)
    print(f"Token '{target_token}' Found: {result}")