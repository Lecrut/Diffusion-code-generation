class IndexFinder:
    def __init__(self, data):
        self.data = data

    def find_final_index(self, target):
        last_index = -1
        for i in range(len(self.data)):
            if self.data[i] == target:
                last_index = i
        return last_index

if __name__ == '__main__':
    sample_list_1 = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value_1 = 5
    index_finder_1 = IndexFinder(sample_list_1)
    final_index_1 = index_finder_1.find_final_index(target_value_1)
    print(final_index_1)

    sample_list_2 = [10, 20, 30, 20, 40]
    target_value_2 = 20
    index_finder_2 = IndexFinder(sample_list_2)
    final_index_2 = index_finder_2.find_final_index(target_value_2)
    print(final_index_2)

    sample_list_3 = [1, 2, 3, 4]
    target_value_3 = 99
    index_finder_3 = IndexFinder(sample_list_3)
    final_index_3 = index_finder_3.find_final_index(target_value_3)
    print(final_index_3)