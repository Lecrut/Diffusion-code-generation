class DictInverter:
    @staticmethod
    def invert(d):
        return {v: k for k, v in d.items()}

if __name__ == '__main__':
    sample_dict = {'x': 1, 'y': 2, 'z': 3}
    inverted_dict = DictInverter.invert(sample_dict)
    print(inverted_dict)