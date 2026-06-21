def get_penultimate_element(data_list):
    if len(data_list) < 2:
        return None
    return data_list[-2]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = []
    sample_list_3 = [42]
    sample_list_4 = [100, 200]
    
    print(get_penultimate_element(sample_list_1))
    print(get_penultimate_element(sample_list_2))
    print(get_penultimate_element(sample_list_3))
    print(get_penultimate_element(sample_list_4))