class ListFinder:
    @staticmethod
    def find_last_index(data, value):
        last_index = -1
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                last_index = i
                break
        return last_index
if __name__ == '__main__':
    my_list = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value = 5
    result = ListFinder.find_last_index(my_list, target_value)
    print(result)
    my_list_2 = [10, 20, 30, 40, 20, 50]
    target_value_2 = 20
    result_2 = ListFinder.find_last_index(my_list_2, target_value_2)
    print(result_2)
    my_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_3 = ListFinder.find_last_index(my_list_3, target_value_3)
    print(result_3)