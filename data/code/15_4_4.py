def get_penultimate_element(data):
    if len(data) < 2:
        return None
    return data[-2]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    result = get_penultimate_element(test_list)
    print(result)

    empty_list = []
    result = get_penultimate_element(empty_list)
    print(result)

    single_list = [99]
    result = get_penultimate_element(single_list)
    print(result)