def retrieve_second_element(elements):
    if len(elements) < 2:
        return None
    second_item = elements[1]
    return second_item

if __name__ == '__main__':
    sample_list_1 = [5, 15, 25, 35]
    sample_list_2 = ['x', 'y']
    sample_list_3 = [True, False]
    sample_list_4 = []
    
    print(retrieve_second_element(sample_list_1))
    print(retrieve_second_element(sample_list_2))
    print(retrieve_second_element(sample_list_3))
    print(retrieve_second_element(sample_list_4))