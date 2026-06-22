def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    half = length // 2
    if length % 2 == 1:
        return sequence[half]
    else:
        left_val = sequence[half - 1]
        right_val = sequence[half]
        return (left_val + right_val) / 2.0

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [1, 3, 5, 7, 9, 11]
    empty_list = []
    
    result_odd = get_middle_element(odd_list)
    result_even = get_middle_element(even_list)
    result_empty = get_middle_element(empty_list)
    
    print(result_odd)
    print(result_even)
    print(result_empty)