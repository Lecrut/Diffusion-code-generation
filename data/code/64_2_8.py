class ListFinder:
    @staticmethod
    def find_last_index(data, value):
        index_map = {}
        for i in range(len(data)):
            if data[i] == value:
                index_map[value] = i
        return index_map.get(value, -1)

if __name__ == '__main__':
    my_list = [7, 4, 2, 8, 4, 3, 4, 9]
    target_value = 4
    result = ListFinder.find_last_index(my_list, target_value)
    print(result)
    another_list = ['a', 'b', 'c', 'b', 'd', 'e']
    another_target = 'b'
    another_result = ListFinder.find_last_index(another_list, another_target)
    print(another_result)