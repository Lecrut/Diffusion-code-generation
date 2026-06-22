class IndexSequence:
    def __init__(self, indices):
        self.indices = indices

    def get_final_index(self):
        if not self.indices:
            return -1
        return self.indices[-1]

    def is_empty(self):
        return len(self.indices) == 0

if __name__ == '__main__':
    sample_indices = [1, 5, 2, 8, 3]
    index_sequence = IndexSequence(sample_indices)
    
    print(index_sequence.get_final_index())
    print(index_sequence.is_empty())