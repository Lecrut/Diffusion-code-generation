def get_middle_element(data):
    mid_index = len(data) // 2
    if len(data) % 2 == 0:
        return data[mid_index - 1], data[mid_index]
    return data[mid_index]

if __name__ == '__main__':
    test_odd = [10, 20, 30, 40, 50]
    test_even = [1, 2, 3, 4, 5, 6]
    print(get_middle_element(test_odd))
    print(get_middle_element(test_even))