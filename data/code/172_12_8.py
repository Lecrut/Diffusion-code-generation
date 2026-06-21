class TokenMatcher:
    def __init__(self, token_to_key_map):
        self._token_to_key = token_to_key_map

    def match_token(self, token):
        return self._token_to_key.get(token)

if __name__ == '__main__':
    sample_mapping = {
        "apple": 1,
        "banana": 2,
        "carrot": 3,
        "broccoli": 4
    }
    matcher = TokenMatcher(sample_mapping)
    print(f"Matching 'apple': {matcher.match_token('apple')}")
    print(f"Matching 'banana': {matcher.match_token('banana')}")
    print(f"Matching 'grape': {matcher.match_token('grape')}")