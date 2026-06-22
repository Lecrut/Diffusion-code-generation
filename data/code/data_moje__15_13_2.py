def get_penultimate_element(data):
    if len(data) < 2:
        return None
    return data[-2]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [42]
    sample_list_3 = []
    result_1 = get_penultimate_element(sample_list_1)
    result_2 = get_penultimate_element(sample_list_2)
    result_3 = get_penultimate_element(sample_list_3)
    print(result_1)
    print(result_2)
    print(result_3)