def find_final_index(indices):
    try:
        if not indices:
            return -1
        if not all((isinstance(i, int) and i >= 0 for i in indices)):
            raise ValueError('All elements must be non-negative integers.')
        return max(indices)
    except TypeError:
        raise ValueError('Input must be a list of valid indices.')
if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5]
    print(find_final_index(sample_list1))
    sample_list2 = [0, 0, 0, 0]
    print(find_final_index(sample_list2))
    sample_list3 = []
    print(find_final_index(sample_list3))
    sample_list4 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(find_final_index(sample_list4))
    try:
        invalid_input = [1, 'a', 3]
        print(find_final_index(invalid_input))
    except ValueError as e:
        print(e)
    try:
        not_a_list = 'not a list'
        print(find_final_index(not_a_list))
    except ValueError as e:
        print(e)