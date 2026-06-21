def get_center_element(sequence):
    if len(sequence) == 0:
        return None
    mid = len(sequence) // 2
    if len(sequence) % 2 == 0:
        return (sequence[mid - 1], sequence[mid])
    else:
        return sequence[mid]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30, 40)
    print(get_center_element(sample_list))
    print(get_center_element(sample_tuple))