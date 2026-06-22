def find_final_index(indices):
    if not indices:
        return -1
    max_value = float('-inf')
    for index in indices:
        if index > max_value:
            max_value = index
    return max_value

if __name__ == '__main__':
    sample_indices_1 = [3, 7, 2, 9, 5]
    print(find_final_index(sample_indices_1))
    
    sample_indices_2 = [42]
    print(find_final_index(sample_indices_2))
    
    sample_indices_3 = []
    print(find_final_index(sample_indices_3))
    
    sample_indices_4 = [10, 20, 30, 40, 50]
    print(find_final_index(sample_indices_4))