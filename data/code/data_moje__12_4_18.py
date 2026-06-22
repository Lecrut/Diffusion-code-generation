def get_middle_value(sequence):
    if not sequence:
        return None
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 1:
        return sequence[mid_index]
    else:
        left_mid = sequence[mid_index - 1]
        right_mid = sequence[mid_index]
        return (left_mid + right_mid) / 2

if __name__ == '__main__':
    odd_list = [3, 1, 4, 1, 5, 9, 2, 6]
    even_list = [10, 20, 30, 40]
    single_element = [42]
    empty_list = []
    
    print(get_middle_value(odd_list))
    print(get_middle_value(even_list))
    print(get_middle_value(single_element))
    print(get_middle_value(empty_list))