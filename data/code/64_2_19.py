class ListFinder:
    @staticmethod
    def find_last_index(data, value):
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                return i
        return -1

if __name__ == '__main__':
    my_list = [7, 4, 3, 4, 5, 6, 4]
    target_value = 4
    result = ListFinder.find_last_index(my_list, target_value)
    print(result)
    
    another_list = ['a', 'b', 'c', 'b', 'd']
    target_value_2 = 'b'
    result_2 = ListFinder.find_last_index(another_list, target_value_2)
    print(result_2)