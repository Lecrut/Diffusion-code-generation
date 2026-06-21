def retrieve_second_element(data):
    MIN_LENGTH = 2
    if len(data) < MIN_LENGTH:
        return None
    return data[1]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4]
    sample_list_2 = ['a', 'b']
    sample_list_3 = [True]
    sample_list_4 = []
    sample_list_5 = [100, 200]

    print(retrieve_second_element(sample_list_1))
    print(retrieve_second_element(sample_list_2))
    print(retrieve_second_element(sample_list_3))
    print(retrieve_second_element(sample_list_4))
    print(retrieve_second_element(sample_list_5))