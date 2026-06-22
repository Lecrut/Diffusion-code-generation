class ListFinder:
    @staticmethod
    def find_last_index(data, value):
        if not isinstance(data, list):
            raise ValueError("The first argument must be a list.")
        if not isinstance(value, (int, float, str)):
            raise ValueError("The second argument must be an int, float, or string.")
        
        last_index = -1
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                last_index = i
                break
        return last_index

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 20]
    target_value = 20
    result = ListFinder.find_last_index(my_list, target_value)
    print(result)

    another_list = ['a', 'b', 'c', 'b', 'd']
    target_value_2 = 'b'
    result_2 = ListFinder.find_last_index(another_list, target_value_2)
    print(result_2)