def get_middle_element(data):
    if not data:
        return None
    mid = len(data) // 2
    if len(data) % 2 == 0:
        return data[mid]
    return data[mid]

if __name__ == '__main__':
    test_odd = [1, 2, 3, 4, 5]
    test_even = [10, 20, 30, 40]
    print(get_middle_element(test_odd))
    print(get_middle_element(test_even))