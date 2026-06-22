def find_middle_element(data):
    if not data:
        return None
    mid_index = len(data) // 2
    if len(data) % 2 == 1:
        return data[mid_index]
    else:
        return data[mid_index]

if __name__ == '__main__':
    test_odd = [1, 2, 3, 4, 5]
    test_even = [10, 20, 30, 40]
    print(find_middle_element(test_odd))
    print(find_middle_element(test_even))