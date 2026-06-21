class KeyWordMapper:
    def __init__(self):
        self.mapping = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five'
        }

    def map_keys_to_words(self, keys):
        return {key: self.mapping.get(key, 'unknown') for key in keys}

if __name__ == '__main__':
    mapper = KeyWordMapper()
    sample_keys = [1, 2, 3, 6]
    print(mapper.map_keys_to_words(sample_keys))