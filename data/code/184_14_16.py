TOKEN_SEPARATOR = ' '

def check_token_presence(text: str, target_token: str) -> bool:
    tokens = text.split(TOKEN_SEPARATOR)
    return any(token.lower() == target_token.lower() for token in tokens)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_token = "fox"
    result = check_token_presence(sample_text, target_token)
    print(f"Token Presence: {result}")