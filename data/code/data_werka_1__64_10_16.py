class IndexFinder:
    def __init__(self, indices):
        if not isinstance(indices, list) or not all(isinstance(i, int) for i in indices):
            raise ValueError("Indices must be a list of integers.")
        self.indices = indices

    def get_final_index(self):
        if not self.indices:
            return -1
        return self.indices[-1]

if __name__ == '__main__':
    sample_indices = [7, 2, 9, 4, 6]
    try:
        index_finder = IndexFinder(sample_indices)
        final_index = index_finder.get_final_index()
        print(final_index)
    except ValueError as e:
        print(e)