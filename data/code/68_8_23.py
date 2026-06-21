def find_first_zero_difference_index(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError("Both lists must have the same length.")
    
    for i in range(len(list_a) - 1):
        if list_a[i] - list_b[i + 1] == 0:
            return i
    
    return -1

if __name__ == '__main__':
    sample_list_a = [5, 10, 15, 20]
    sample_list_b = [3, 10, 7, 20]
    
    index = find_first_zero_difference_index(sample_list_a, sample_list_b)
    print(index)