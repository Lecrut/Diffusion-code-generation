class DictReverser:
    def __init__(self, data):
        self._data = dict(data)
    
    def reverse_dict(self):
        return {k: self._data[k] for k in reversed(sorted(self._data.keys()))}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    reverser = DictReverser(sample_dict)
    print("Original dictionary:", sample_dict)
    reversed_dict = reverser.reverse_dict()
    print("Reversed dictionary by key:", reversed_dict)