def get_center_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    index = length // 2
    if length % 2 == 0:
        index -= 1
    return sequence[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result_list = get_center_element(sample_list)
    print(result_list)
    
    sample_tuple = (1, 2, 3, 4)
    result_tuple = get_center_element(sample_tuple)
    print(result_tuple)
    
    sample_odd = (100, 200, 300)
    result_odd = get_center_element(sample_odd)
    print(result_odd)