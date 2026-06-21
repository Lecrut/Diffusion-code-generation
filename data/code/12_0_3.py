def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return sequence[length // 2 - 1]

if __name__ == '__main__':
    odd_seq = [10, 20, 30, 40, 50]
    even_seq = [10, 20, 30, 40, 50, 60]
    empty_seq = []
    single_seq = [42]

    print(get_middle_element(odd_seq))
    print(get_middle_element(even_seq))
    print(get_middle_element(empty_seq))
    print(get_middle_element(single_seq))