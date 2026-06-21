class NestedDictRetriever:
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
    sample_data = {
        'level1': {
            'level2a': {
                'level3': 'value1'
            },
            'level2b': 'value2'
        }
    }

    retriever = NestedDictRetriever(sample_data)
    
    keys_path1 = ['level1', 'level2a', 'level3']
    keys_path2 = ['level1', 'level2b']
    keys_path3 = ['level1', 'nonexistent']

    print("Retrieved value for path1:", retriever.get_element(keys_path1))
    print("Retrieved value for path2:", retriever.get_element(keys_path2))
    print("Retrieved value for path3:", retriever.get_element(keys_path3))