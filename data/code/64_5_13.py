class ReverseListSearch:
    DEFAULT_TARGET = 20

    @staticmethod
    def find_last_occurrence_reverse(data, target):
        n = len(data)
        for i in range(n - 1, -1, -1):
            if data[i] == target:
                return i
        return -1

if __name__ == '__main__':
    large_list_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value_1 = 70
    search_instance = ReverseListSearch()
    result_index_1 = search_instance.find_last_occurrence_reverse(large_list_1, target_value_1)
    print(result_index_1)

    large_list_2 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
    target_value_2 = ReverseListSearch.DEFAULT_TARGET
    result_index_2 = search_instance.find_last_occurrence_reverse(large_list_2, target_value_2)
    print(result_index_2)

    large_list_3 = [1, 3, 5, 7, 9, 11, 13]
    target_value_3 = 8
    result_index_3 = search_instance.find_last_occurrence_reverse(large_list_3, target_value_3)
    print(result_index_3)

    large_list_4 = [20, 20, 20, 20, 20]
    target_value_4 = 20
    result_index_4 = search_instance.find_last_occurrence_reverse(large_list_4, target_value_4)
    print(result_index_4)

    large_list_5 = []
    target_value_5 = 10
    result_index_5 = search_instance.find_last_occurrence_reverse(large_list_5, target_value_5)
    print(result_index_5)