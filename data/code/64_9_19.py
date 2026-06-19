def validate_input(data, target):
    if not isinstance(data, list):
        raise TypeError("Data must be a list.")
    if not data:
        raise ValueError("Data list cannot be empty.")
    if not isinstance(target, (int, float, str)):
        raise TypeError("Target must be an integer, float, or string.")

def find_final_index(data, target):
    validate_input(data, target)
    last_index = -1
    for index in range(len(data)):
        if data[index] == target:
            last_index = index
    return last_index

if __name__ == '__main__':
    sample_list_1 = [3, 5, 7, 5, 9, 5]
    target_value_1 = 5
    final_index_1 = find_final_index(sample_list_1, target_value_1)
    print(final_index_1)

    sample_list_2 = ['a', 'b', 'c', 'b', 'd']
    target_value_2 = 'b'
    final_index_2 = find_final_index(sample_list_2, target_value_2)
    print(final_index_2)

    sample_list_3 = [1.1, 2.2, 3.3, 2.2]
    target_value_3 = 2.2
    final_index_3 = find_final_index(sample_list_3, target_value_3)
    print(final_index_3)