def is_valid_index_list(indices):
    return isinstance(indices, list) and all(isinstance(i, int) for i in indices)

def find_final_index(indices):
    if not is_valid_index_list(indices):
        raise ValueError("Input must be a list of integers.")
    
    if not indices:
        return -1
    
    return max(indices)

if __name__ == '__main__':
    sample1 = [3, 7, 2, 9, 5]
    print(find_final_index(sample1))
    
    sample2 = [10, 20, 30, 40, 50]
    print(find_final_index(sample2))
    
    sample3 = []
    print(find_final_index(sample3))
    
    sample4 = [100]
    print(find_final_index(sample4))