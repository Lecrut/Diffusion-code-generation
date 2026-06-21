def get_center_element(sequence):
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1], sequence[length // 2])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_center_element(sample_list))
    sample_tuple = (10, 20, 30, 40)
    print(get_center_element(sample_tuple))
    sample_odd_tuple = (7, 8, 9)
    print(get_center_element(sample_odd_tuple))