class ListFinder:
    def __init__(self):
        self.last_index = -1

    def find_last_index(self, data, value):
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                self.last_index = i
                break
        return self.last_index

if __name__ == '__main__':
    my_list = [7, 3, 5, 3, 9, 3]
    target_value = 3
    finder = ListFinder()
    result = finder.find_last_index(my_list, target_value)
    print(result)

    my_list_2 = ['a', 'b', 'c', 'b', 'd']
    target_value_2 = 'b'
    result_2 = finder.find_last_index(my_list_2, target_value_2)
    print(result_2)