class IndexFinder:
    def __init__(self, data):
        self.data = data

    def find_all_indices(self, item):
        for i, x in enumerate(self.data):
            if x == item:
                yield i

    def find_final_index(self, item):
        indices = list(self.find_all_indices(item))
        return indices[-1] if indices else -1

if __name__ == '__main__':
    sample_data = [10, 20, 30, 20, 40, 20, 50]
    target_item = 20
    finder = IndexFinder(sample_data)
    
    all_indices = list(finder.find_all_indices(target_item))
    print("All indices:", all_indices)
    
    final_index = finder.find_final_index(target_item)
    print("Final index of the last occurrence:", final_index)