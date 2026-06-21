class TokenChecker:
    TOKEN_DELIMITER = " "

    @staticmethod
    def check_token_presence(text: str, target_token: str) -> bool:
        return target_token in text.split(TokenChecker.TOKEN_DELIMITER)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_token = "fox"
    result = TokenChecker.check_token_presence(sample_text, target_token)
    print(f"Token Presence: {result}")