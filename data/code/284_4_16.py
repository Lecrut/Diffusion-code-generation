class DictReverser:
    @staticmethod
    def reverse_keys(d):
        return {k: d[k] for k in reversed(list(d.keys()))}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original dictionary:", sample_dict)
    reversed_dict = DictReverser.reverse_keys(sample_dict)
    print("Reversed dictionary:", reversed_dict)