def get_middle_element(sequence):
    if not hasattr(sequence, '__len__'):
        raise TypeError("Input must be a sequence type.")
    
    length = len(sequence)
    
    if length == 0:
        raise ValueError("Cannot get middle element of an empty sequence.")
    
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        lower_index = (length // 2) - 1
        upper_index = length // 2
        return (sequence[lower_index] + sequence[upper_index]) / 2

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [10, 20, 30, 40]
    
    result_odd = get_middle_element(odd_list)
    result_even = get_middle_element(even_list)
    
    print(result_odd)
    print(result_even)