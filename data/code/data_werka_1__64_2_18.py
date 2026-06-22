class ListFinder:
    @staticmethod
    def find_last_index(data, value):
        last_index = -1
        for index in range(len(data)):
            if data[index] == value:
                last_index = index
        return last_index

if __name__ == '__main__':
    sample_list_1 = [7, 3, 5, 8, 3, 9, 3]
    target_value_1 = 3
    finder = ListFinder()
    result_1 = finder.find_last_index(sample_list_1, target_value_1)
    print(result_1)

    sample_list_2 = [10, 25, 30, 45, 25, 60]
    target_value_2 = 25
    result_2 = finder.find_last_index(sample_list_2, target_value_2)
    print(result_2)

    sample_list_3 = [100, 200, 300, 400, 500]
    target_value_3 = 600
    result_3 = finder.find_last_index(sample_list_3, target_value_3)
    print(result_3)