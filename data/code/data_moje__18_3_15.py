def get_center_element(data):
    if not data:
        raise ValueError("List cannot be empty")
    return data[len(data) // 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_center_element(sample_list)
    print(result)
    sample_list_two = [1, 2, 3, 4]
    result_two = get_center_element(sample_list_two)
    print(result_two)