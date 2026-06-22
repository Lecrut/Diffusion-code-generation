def get_middle_value(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    mid_index = len(data) // 2
    if len(data) % 2 == 0:
        mid_index -= 1
    return data[mid_index]

if __name__ == '__main__':
    print(get_middle_value([1, 2, 3]))
    print(get_middle_value([1, 2, 3, 4]))
    print(get_middle_value([5]))
    print(get_middle_value([10, 20]))
    print(get_middle_value([1, 2, 3, 4, 5, 6, 7]))
    print(get_middle_value([1, 2, 3, 4, 5, 6]))