class KeyMapper:
    @staticmethod
    def map_keys_to_true(keys):
        return {key: True for key in keys}

if __name__ == '__main__':
    mapper = KeyMapper()
    sample_keys = ['apple', 'banana', 'cherry']
    result_dict = mapper.map_keys_to_true(sample_keys)
    print(result_dict)