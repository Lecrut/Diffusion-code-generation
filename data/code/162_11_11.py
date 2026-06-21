class KeyMapper:
    def __init__(self, keys):
        self.keys = keys

    def map_to_true(self):
        return {key: True for key in self.keys}

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    mapper = KeyMapper(sample_keys)
    result_dict = mapper.map_to_true()
    print(result_dict)