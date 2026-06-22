def retrieve_second_element(elements):
    if len(elements) < 2:
        return None
    return elements[1]

if __name__ == '__main__':
    sample_data_1 = [5, 15, 25, 35]
    sample_data_2 = ['hello', 'world']
    sample_data_3 = [True, False]
    sample_data_4 = []
    sample_data_5 = [42]

    print(retrieve_second_element(sample_data_1))
    print(retrieve_second_element(sample_data_2))
    print(retrieve_second_element(sample_data_3))
    print(retrieve_second_element(sample_data_4))
    print(retrieve_second_element(sample_data_5))