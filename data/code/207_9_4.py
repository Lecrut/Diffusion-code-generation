def find_max_nested(nested_list):
    if not nested_list:
        raise ValueError("Input list is empty")
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
    max_val = find_max_nested(data)
    print(max_val)