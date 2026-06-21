def get_center_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return sequence[length // 2 - 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_center_element(sample_list))

    sample_tuple = (100, 200, 300, 400)
    print(get_center_element(sample_tuple))