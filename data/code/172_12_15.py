class TokenMapper:
    def __init__(self, key_to_token_mapping):
        self._key_to_token = key_to_token_mapping

    @staticmethod
    def from_lists(keys, tokens):
        return TokenMapper(dict(zip(keys, tokens)))

    def map_key_to_token(self, key):
        return self._key_to_token.get(key)

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 4]
    sample_tokens = ["one", "two", "three", "four"]
    mapper = TokenMapper.from_lists(sample_keys, sample_tokens)
    print(f"Mapping 1: {mapper.map_key_to_token(1)}")
    print(f"Mapping 2: {mapper.map_key_to_token(2)}")
    print(f"Mapping 3: {mapper.map_key_to_token(3)}")
    print(f"Mapping 5: {mapper.map_key_to_token(5)}")