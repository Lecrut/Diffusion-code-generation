class ListFinder:
    @staticmethod
    def find_last_index(data, value):
        if not isinstance(data, list) or not data:
            return -1
        last_index = -1
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                last_index = i
                break
        return last_index

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 60, 70]
    target_value = 30
    result = ListFinder.find_last_index(my_list, target_value)
    print(result)

    my_list_2 = [1, 2, 3, 4, 2, 5, 2]
    target_value_2 = 2
    result_2 = ListFinder.find_last_index(my_list_2, target_value_2)
    print(result_2)

    my_list_3 = []
    target_value_3 = 10
    result_3 = ListFinder.find_last_index(my_list_3, target_value_3)
    print(result_3)