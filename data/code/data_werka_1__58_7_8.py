def get_first_element(data_list):
    if not data_list:
        return None
    return data_list[0]

if __name__ == '__main__':
    sample1 = [5, 6, 7]
    sample2 = ['x', 'y', 'z']
    empty_sample = []
    single_element_sample = [123]
    
    print(f"First element of {sample1}: {get_first_element(sample1)}")
    print(f"First element of {sample2}: {get_first_element(sample2)}")
    print(f"First element of {empty_sample}: {get_first_element(empty_sample)}")
    print(f"First element of {single_element_sample}: {get_first_element(single_element_sample)}")