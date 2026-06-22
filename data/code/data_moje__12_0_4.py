def get_middle_element(sequence):
    if not sequence:
        return None
    n = len(sequence)
    mid = n // 2
    if n % 2 == 1:
        return sequence[mid]
    else:
        return sequence[mid - 1]

if __name__ == '__main__':
    odd_seq = [1, 2, 3, 4, 5]
    even_seq = [1, 2, 3, 4]
    single_element = [42]
    empty_seq = []

    print(get_middle_element(odd_seq))
    print(get_middle_element(even_seq))
    print(get_middle_element(single_element))
    print(get_middle_element(empty_seq))