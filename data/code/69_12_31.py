class NestedDataRetriever:

    def __init__(self, data):
        self.data = data

    def retrieve(self, keys):
        try:
            value = self.data
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError) as e:
            raise ValueError('Invalid keys or data structure') from e
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': 'hello'}, 'e': [1, 2, 3]}, 'f': True, 'g': {'h': {'i': {'j': 99}}}}
    retriever = NestedDataRetriever(sample_data)
    keys_to_retrieve_1 = ['a', 'b', 'c']
    result_1 = retriever.retrieve(keys_to_retrieve_1)
    print(result_1)
    keys_to_retrieve_2 = ['a', 'e', 1]
    result_2 = retriever.retrieve(keys_to_retrieve_2)
    print(result_2)
    keys_to_retrieve_3 = ['g', 'h', 'i', 'j']
    result_3 = retriever.retrieve(keys_to_retrieve_3)
    print(result_3)