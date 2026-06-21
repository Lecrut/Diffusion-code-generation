class TokenMapper:
    def __init__(self, token_to_key_mapping):
        self._token_to_key = token_to_key_mapping

    def map_token_to_key(self, token):
        return self._token_to_key.get(token)

if __name__ == '__main__':
    sample_mapping = {
        "dog": "animal1",
        "cat": "animal2",
        "tree": "plant1",
        "sun": "celestial1"
    }
    mapper = TokenMapper(sample_mapping)
    print(f"Mapping 'dog': {mapper.map_token_to_key('dog')}")
    print(f"Mapping 'cat': {mapper.map_token_to_key('cat')}")
    print(f"Mapping 'bird': {mapper.map_token_to_key('bird')}")