def get_penultimate_element(data):
    if len(data) < 2:
        return None
    return data[-2]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5]
    sample_list_3 = []
    sample_list_4 = ['a', 'b', 'c']
    
    print(get_penultimate_element(sample_list_1))
    print(get_penultimate_element(sample_list_2))
    print(get_penultimate_element(sample_list_3))
    print(get_penultimate_element(sample_list_4))