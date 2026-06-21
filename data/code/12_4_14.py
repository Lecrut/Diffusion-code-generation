def get_middle_value(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 1:
        mid_index = length // 2
        return sequence[mid_index]
    mid_index_1 = (length // 2) - 1
    mid_index_2 = length // 2
    val1 = sequence[mid_index_1]
    val2 = sequence[mid_index_2]
    return (val1 + val2) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [2, 4, 6, 8]
    print(get_middle_value(odd_list))
    print(get_middle_value(even_list))