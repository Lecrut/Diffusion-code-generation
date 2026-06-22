def get_middle_element(data):
    if not data:
        raise ValueError("List must not be empty")
    length = len(data)
    if length % 2 == 0:
        return data[length // 2 - 1]
    return data[length // 2]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([10]))
    print(get_middle_element([10, 20]))
    print(get_middle_element([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(get_middle_element([1, 2, 3, 4, 5, 6, 7, 8]))