class NestedDictFetcher:

    def __init__(self, data):
        self.data = data

    def get_elements(self, *keys):
        result = []
        current_level = self.data
        for key in keys:
            if isinstance(current_level, dict) and key in current_level:
                current_level = current_level[key]
            else:
                return None
        if isinstance(current_level, list):
            result.extend(current_level)
        elif isinstance(current_level, dict):
            result.append(current_level)
        return result
if __name__ == '__main__':
    sample_data = {'a': {'b': [1, 2, 3], 'c': {'d': 4}}, 'e': {'f': [5, 6]}}
    fetcher = NestedDictFetcher(sample_data)
    print(fetcher.get_elements('a', 'b'))
    print(fetcher.get_elements('a', 'c', 'd'))
    print(fetcher.get_elements('e', 'f'))
    print(fetcher.get_elements('g'))