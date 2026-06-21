class DictInverter:
    @staticmethod
    def invert_dict(d):
        return {v: k for k, v in d.items() if hash(v) == v and isinstance(v, (int, float, str, bool))}

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12
    }
    inverted_dict = DictInverter.invert_dict(sample_dict)
    print(inverted_dict)