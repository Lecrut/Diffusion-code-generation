def get_center_element(sequence):
    n = len(sequence)
    if n == 0:
        return None
    center_index = n // 2
    return sequence[center_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300, 400)
    print(get_center_element(sample_list))
    print(get_center_element(sample_tuple))