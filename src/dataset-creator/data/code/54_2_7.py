def find_middle_index(sequence):
    if not sequence:
        return None
    length = len(sequence)
    middle_value = (length - 1) // 2 + 1
    for i in range(length):
        index = i * middle_value
        if index >= length or index < 0:
            break
        value_at_index = sequence[index]
        return value_at_index
if __name__ == '__main__':
    even_sequence = [1, 2, 3, 4, 5, 6]
    odd_sequence = [7, 8, 9, 10, 11]
    result_even = find_middle_index(even_sequence)
    result_odd = find_middle_index(odd_sequence)
    print(result_even)
    print(result_odd)