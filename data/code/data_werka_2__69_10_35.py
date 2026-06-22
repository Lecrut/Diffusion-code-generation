class StringIndexer:
    def __init__(self, s):
        if not isinstance(s, str):
            raise ValueError('The input must be a string.')
        self.s = s

    def get_characters_by_indices(self, indices):
        if not all(isinstance(i, int) for i in indices):
            raise ValueError('All elements in the list must be integers.')
        valid_indices = [i for i in indices if 0 <= i < len(self.s)]
        return ''.join(self.s[i] for i in valid_indices)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    indexer = StringIndexer(sample_string)
    sample_indices_1 = [0, 7, 8, 12]
    print(indexer.get_characters_by_indices(sample_indices_1))
    sample_indices_2 = [5, 10, 15]
    print(indexer.get_characters_by_indices(sample_indices_2))