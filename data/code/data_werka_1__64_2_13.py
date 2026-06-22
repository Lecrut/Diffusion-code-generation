class ListFinder:

    @staticmethod
    def find_last_index(data, value):
        index_map = {}
        for i in range(len(data)):
            if data[i] == value:
                index_map[value] = i
        return index_map.get(value, -1)
if __name__ == '__main__':
    my_list = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value = 5
    result = ListFinder.find_last_index(my_list, target_value)
    print(result)
    my_list_2 = ['a', 'b', 'c', 'd', 'b', 'e']
    target_value_2 = 'b'
    result_2 = ListFinder.find_last_index(my_list_2, target_value_2)
    print(result_2)