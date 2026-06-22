class DictReverser:
    def __init__(self, data):
        self._data = dict(data)
    
    def reverse_keys(self):
        reversed_dict = {key: self._data[key] for key in reversed(list(self._data))}
        return reversed_dict

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    reverser = DictReverser(sample_dict)
    print("Original dictionary:", sample_dict)
    reversed_dict = reverser.reverse_keys()
    print("Dictionary after reversing keys:", reversed_dict)