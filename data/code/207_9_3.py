def find_max_in_nested_list(nested_list):
    if not nested_list:
        raise ValueError("Input list cannot be empty")
    max_element = nested_list[0][0]
    for sublist in nested_list:
        for element in sublist:
            if element > max_element:
                max_element = element
    return max_element
if __name__ == '__main__':
    data = [
        [1, 5, 2],
        [8, 3, 9],
        [4, 6, 7]
    ]
    print(find_max_in_nested_list(data))
    data_2 = [
        [-10, -5],
        [-20, -1]
    ]
    print(find_max_in_nested_list(data_2))
    data_3 = [
        [100],
        [50, 200]
    ]
    print(find_max_in_nested_list(data_3))