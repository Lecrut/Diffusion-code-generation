class ListFinder:
    def find_last_index(self, data, value):
        last_index = -1
        for index in range(len(data) - 1, -1, -1):
            if data[index] == value:
                last_index = index
                break
        return last_index

if __name__ == '__main__':
    my_list = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value = 5
    finder = ListFinder()
    result = finder.find_last_index(my_list, target_value)
    print(result)

    another_list = ['a', 'b', 'c', 'd', 'b', 'e']
    target_letter = 'b'
    result_2 = finder.find_last_index(another_list, target_letter)
    print(result_2)

    third_list = [10, 20, 30, 40, 50]
    target_number = 60
    result_3 = finder.find_last_index(third_list, target_number)
    print(result_3)