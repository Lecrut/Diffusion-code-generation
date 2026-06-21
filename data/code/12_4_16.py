def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    
    sorted_seq = sorted(sequence)
    length = len(sorted_seq)
    middle_index = length // 2
    
    if length % 2 == 0:
        first_middle = sorted_seq[middle_index - 1]
        second_middle = sorted_seq[middle_index]
        return (first_middle + second_middle) / 2
    else:
        return sorted_seq[middle_index]

if __name__ == '__main__':
    odd_list = [3, 1, 4, 1, 5, 9, 2]
    even_list = [1, 2, 3, 4]
    single_element = [42]
    
    result_odd = get_middle_value(odd_list)
    result_even = get_middle_value(even_list)
    result_single = get_middle_value(single_element)
    
    print(result_odd)
    print(result_even)
    print(result_single)