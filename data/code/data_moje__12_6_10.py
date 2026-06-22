def get_center_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    return sequence[length // 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    print(get_center_element(sample_list))
    print(get_center_element(sample_tuple))