def get_penultimate_element(data):
    if len(data) < 2:
        return None
    return data[-2]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [10]
    sample_list_3 = []
    print(get_penultimate_element(sample_list_1))
    print(get_penultimate_element(sample_list_2))
    print(get_penultimate_element(sample_list_3))