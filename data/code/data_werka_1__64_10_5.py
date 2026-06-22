class IndexFinder:
    def __init__(self, indices):
        self.indices = indices

    def find_final_index(self):
        if not self.indices:
            return -1
        return self.indices[-1]

if __name__ == '__main__':
    sample_indices = [10, 20, 30, 40, 50]
    index_finder = IndexFinder(sample_indices)
    
    final_index = index_finder.find_final_index()
    print(final_index)

    empty_indices = []
    empty_finder = IndexFinder(empty_indices)
    print(empty_finder.find_final_index())