def find_max_nested(nested_list):
    if not nested_list:
        raise ValueError("Input list cannot be empty")
    max_val = nested_list[0][0]
    for sublist in nested_list:
        for element in sublist:
            if element > max_val:
                max_val = element
    return max_val
if __name__ == '__main__':
    data = [
        [1, 5, 2],
        [8, 3, 9],
        [4, 7, 6]
    ]
    print(find_max_nested(data))
    data_2 = [
        [-10, -5],
        [0, 100],
        [-20, 50]
    ]
    print(find_max_nested(data_2))
    data_3 = [
        [1],
        [99],
        [42]
    ]
    print(find_max_nested(data_3))