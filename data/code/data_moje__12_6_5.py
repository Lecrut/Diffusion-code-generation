def get_center_element(sequence):
    length = len(sequence)
    center_index = length // 2
    return sequence[center_index]

if __name__ == '__main__':
    list_sample = [10, 20, 30, 40, 50]
    tuple_sample = (100, 200, 300, 400, 500, 600, 700)
    list_result = get_center_element(list_sample)
    tuple_result = get_center_element(tuple_sample)
    print(list_result)
    print(tuple_result)