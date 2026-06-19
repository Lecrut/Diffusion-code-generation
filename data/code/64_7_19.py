class IndexFinder:
    @staticmethod
    def find_all_indices(data, item):
        for i, x in enumerate(data):
            if x == item:
                yield i

    @staticmethod
    def find_final_index(data, item):
        indices = list(IndexFinder.find_all_indices(data, item))
        return indices[-1] if indices else -1

if __name__ == '__main__':
    sample_data = [4, 9, 2, 9, 7, 9, 6]
    target_item = 9
    final_index = IndexFinder.find_final_index(sample_data, target_item)
    print(final_index)