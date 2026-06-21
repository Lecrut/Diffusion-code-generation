def get_middle_element(data):
    return data[len(data) // 2]

if __name__ == '__main__':
    test_list_1 = [10, 20, 30, 40, 50]
    test_list_2 = ['a', 'b', 'c', 'd']
    result_1 = get_middle_element(test_list_1)
    result_2 = get_middle_element(test_list_2)
    print(result_1)
    print(result_2)