def find_final_index(indices):
    if not isinstance(indices, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements in the list must be integers.")
    if not indices:
        return -1
    return indices[-1]

class IndexFinder:
    def __init__(self, indices):
        self.indices = indices

    def get_final_index(self):
        return find_final_index(self.indices)

if __name__ == '__main__':
    sample_indices = [7, 3, 9, 2, 6]
    index_finder = IndexFinder(sample_indices)
    final_index = index_finder.get_final_index()
    print(final_index)