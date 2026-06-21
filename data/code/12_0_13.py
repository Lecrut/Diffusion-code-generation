def get_middle_element(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 1:
        middle_index = length // 2
        return sequence[middle_index]
    else:
        upper_index = length // 2
        return sequence[upper_index]

if __name__ == '__main__':
    odd_sequence = [10, 20, 30, 40, 50]
    even_sequence = [1, 2, 3, 4]
    result_odd = get_middle_element(odd_sequence)
    result_even = get_middle_element(even_sequence)
    print(result_odd)
    print(result_even)