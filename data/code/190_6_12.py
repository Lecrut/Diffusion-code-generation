class KeyVerifier:
    @staticmethod
    def convert_to_set(data):
        return set(data)

    @staticmethod
    def key_exists(key_set, key):
        return key in key_set

if __name__ == '__main__':
    sample_list = [{'a': 1}, {'b': 2}, {'c': 3}]
    key_to_check = 'b'
    converted_set = KeyVerifier.convert_to_set(sample_list)
    result = KeyVerifier.key_exists(converted_set, key_to_check)
    print(f"Key exists: {result}")