class DictionaryInverter:
    @staticmethod
    def invert_dict(d):
        return {v: k for k, v in d.items() if isinstance(v, hashable)}

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12
    }
    inverted_dict = DictionaryInverter.invert_dict(sample_dict)
    print(inverted_dict)