def get_center_element(data):
    if not data:
        return None
    n = len(data)
    return data[n // 2]

if __name__ == '__main__':
    list_sample = [10, 20, 30, 40, 50]
    tuple_sample = (1, 2, 3, 4)
    empty_sample = []
    odd_sample = (99,)

    print(get_center_element(list_sample))
    print(get_center_element(tuple_sample))
    print(get_center_element(empty_sample))
    print(get_center_element(odd_sample))