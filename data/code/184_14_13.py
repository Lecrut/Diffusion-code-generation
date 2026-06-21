def contains_token(input_string: str, target_token: str) -> bool:
    words = input_string.split()
    return target_token.lower() in [word.lower() for word in words]

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    token_to_check = "fox"
    result = contains_token(sample_text, token_to_check)
    print(f"Token '{token_to_check}' found: {result}")