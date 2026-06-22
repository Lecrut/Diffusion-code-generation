def find_final_index(indices):
    if not isinstance(indices, list):
        raise TypeError('Input must be a list')
    if not all((isinstance(i, int) for i in indices)):
        raise ValueError('All elements in the list must be integers')
    if not indices:
        return -1
    return max(indices)
if __name__ == '__main__':
    try:
        sample1 = [1, 5, 3, 8, 2]
        print(find_final_index(sample1))
        sample2 = [10, 20, 5]
        print(find_final_index(sample2))
        sample3 = [42]
        print(find_final_index(sample3))
        sample4 = []
        print(find_final_index(sample4))
        invalid_input1 = 'not a list'
        print(find_final_index(invalid_input1))
        invalid_input2 = [1, 'a', 3]
        print(find_final_index(invalid_input2))
    except Exception as e:
        print(f'An error occurred: {e}')