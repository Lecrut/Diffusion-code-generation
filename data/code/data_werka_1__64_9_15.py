def find_final_index(data, target):
    def validate_input():
        if not isinstance(data, list):
            raise ValueError("Data must be a list.")
        if not isinstance(target, (int, float, str)):
            raise ValueError("Target must be an int, float, or string.")

    validate_input()
    last_index = -1
    for index, element in enumerate(data):
        if element == target:
            last_index = index
    return last_index

if __name__ == '__main__':
    sample_list_1 = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value_1 = 5
    print(find_final_index(sample_list_1, target_value_1))

    sample_list_2 = ['a', 'b', 'c', 'b', 'd']
    target_value_2 = 'b'
    print(find_final_index(sample_list_2, target_value_2))

    sample_list_3 = [10.5, 20.5, 30.5, 20.5]
    target_value_3 = 20.5
    print(find_final_index(sample_list_3, target_value_3))

    sample_list_4 = [True, False, True, True]
    target_value_4 = True
    print(find_final_index(sample_list_4, target_value_4))