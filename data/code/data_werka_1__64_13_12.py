def find_final_index(indices):
    DEFAULT_RETURN_VALUE = -1
    if not indices:
        return DEFAULT_RETURN_VALUE
    return max(indices)

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 5, 3, 8, 2]
    print(find_final_index(SAMPLE_LIST_1))
    
    SAMPLE_LIST_2 = [10, 20, 5]
    print(find_final_index(SAMPLE_LIST_2))
    
    SAMPLE_LIST_3 = [42]
    print(find_final_index(SAMPLE_LIST_3))
    
    SAMPLE_LIST_4 = []
    print(find_final_index(SAMPLE_LIST_4))