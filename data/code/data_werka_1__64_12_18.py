class IndexFinder:
    EMPTY_LIST_RESULT = -1

    @staticmethod
    def find_final_item_index(indices):
        if not indices:
            return IndexFinder.EMPTY_LIST_RESULT
        return max(indices)

if __name__ == '__main__':
    sample_lists = [
        [1, 5, 3, 8, 2],
        [],
        [42],
        [-5, -1, -10],
        [10, 20, 5],
        [100],
        [5, 5, 5],
        [-10, 0, -5]
    ]

    for idx, lst in enumerate(sample_lists):
        print(f"Input: {lst}, Result: {IndexFinder.find_final_item_index(lst)}")