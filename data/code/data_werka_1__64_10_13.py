class IndexSequence:
    def __init__(self, indices):
        self.indices = indices

    def get_final_index(self):
        if not self.indices:
            return -1
        return self.indices[-1]

if __name__ == '__main__':
    sample_indices = [2, 4, 6, 8, 10]
    sequence = IndexSequence(sample_indices)
    print(sequence.get_final_index())