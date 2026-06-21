class NestedDictExtractor:

    def __init__(self, data):
        self.data = data

    def get_element(self, keys):
        result = self.data
        for key in keys:
            if isinstance(result, dict) and key in result:
                result = result[key]
            else:
                return None
        return result
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 1, 'd': 2}, 'e': 3}, 'f': {'g': 4}}
    extractor = NestedDictExtractor(sample_data)
    print('Extracting elements from nested dictionary:')
    keys1 = ['a', 'b', 'c']
    print(f'Element with keys {keys1}: {extractor.get_element(keys1)}')
    keys2 = ['f', 'g']
    print(f'Element with keys {keys2}: {extractor.get_element(keys2)}')
    keys3 = ['a', 'e']
    print(f'Element with keys {keys3}: {extractor.get_element(keys3)}')
    keys4 = ['a', 'b', 'z']
    print(f'Element with keys {keys4}: {extractor.get_element(keys4)}')