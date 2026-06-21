def get_central_element(data):
    if not data:
        return None
    return data[len(data) // 2]

if __name__ == '__main__':
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [1, 2, 3, 4, 5, 6]
    empty_list = []
    single_element = [99]

    result_odd = get_central_element(sample_list_odd)
    result_even = get_central_element(sample_list_even)
    result_empty = get_central_element(empty_list)
    result_single = get_central_element(single_element)

    print(result_odd)
    print(result_even)
    print(result_empty)
    print(result_single)