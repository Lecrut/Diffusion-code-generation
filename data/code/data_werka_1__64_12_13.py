class IndexFinder:
    def __init__(self, indices):
        self.indices = indices

    def find_final_item_index(self):
        if not self.indices:
            return -1
        return max(self.indices)

if __name__ == '__main__':
    sample_lists = [
        [1, 5, 3, 8, 2],
        [10, 20, 5],
        [],
        [42],
        [-5, -1, -10]
    ]

    for i, lst in enumerate(sample_lists):
        index_finder = IndexFinder(lst)
        print(f"Input: {lst}, Result: {index_finder.find_final_item_index()}")