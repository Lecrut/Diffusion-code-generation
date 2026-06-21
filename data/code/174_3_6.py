class DictInverter:
    def invert(self, d):
        return {v: k for k, v in d.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    inverter = DictInverter()
    inverted_dict = inverter.invert(sample_dict)
    print(inverted_dict)