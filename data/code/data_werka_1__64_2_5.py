class ListFinder:

    @staticmethod
    def find_last_index(data, value):
        if not isinstance(data, list):
            raise ValueError('The data must be a list.')
        last_index = -1
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                last_index = i
                break
        return last_index
if __name__ == '__main__':
    try:
        sample_list_1 = [7, 3, 5, 8, 3, 2, 3]
        target_value_1 = 3
        result_1 = ListFinder.find_last_index(sample_list_1, target_value_1)
        print(result_1)
        sample_list_2 = ['a', 'b', 'c', 'd', 'e']
        target_value_2 = 'z'
        result_2 = ListFinder.find_last_index(sample_list_2, target_value_2)
        print(result_2)
        invalid_input = 'not a list'
        result_3 = ListFinder.find_last_index(invalid_input, 5)
        print(result_3)
    except ValueError as e:
        print(e)