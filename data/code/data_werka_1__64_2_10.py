class ListFinder:
    @staticmethod
    def find_last_index(data, value):
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                return i
        return -1

if __name__ == '__main__':
    my_list = [7, 3, 5, 7, 2, 7]
    target_value = 7
    result = ListFinder.find_last_index(my_list, target_value)
    print(result)

    another_list = [10, 20, 30, 40, 50]
    target_value_2 = 60
    result_2 = ListFinder.find_last_index(another_list, target_value_2)
    print(result_2)