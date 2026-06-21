def get_penultimate_element(data):
    if len(data) < 2:
        return None
    return data[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    single_element = [42]
    two_elements = ['a', 'b']
    
    print(get_penultimate_element(sample_list))
    print(get_penultimate_element(empty_list))
    print(get_penultimate_element(single_element))
    print(get_penultimate_element(two_elements))