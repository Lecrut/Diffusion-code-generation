def get_middle_element(data):
    return data[len(data) // 2]

if __name__ == '__main__':
    test_list_1 = [10, 20, 30, 40, 50]
    test_list_2 = [1, 2, 3, 4]
    print(get_middle_element(test_list_1))
    print(get_middle_element(test_list_2))