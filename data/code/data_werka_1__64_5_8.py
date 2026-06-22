class ReverseSearch:
    def __init__(self, data):
        self.data = data

    def find_last_occurrence(self, target):
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == target:
                return i
        return -1

if __name__ == '__main__':
    large_list_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value_1 = 70
    searcher_1 = ReverseSearch(large_list_1)
    result_index_1 = searcher_1.find_last_occurrence(target_value_1)
    print(result_index_1)

    large_list_2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    target_value_2 = 85
    searcher_2 = ReverseSearch(large_list_2)
    result_index_2 = searcher_2.find_last_occurrence(target_value_2)
    print(result_index_2)

    large_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    searcher_3 = ReverseSearch(large_list_3)
    result_index_3 = searcher_3.find_last_occurrence(target_value_3)
    print(result_index_3)