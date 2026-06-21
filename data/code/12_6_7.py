def get_center_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    index = (length - 1) // 2
    return sequence[index]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    test_tuple = (100, 200, 300, 400)
    
    result_list = get_center_element(test_list)
    result_tuple = get_center_element(test_tuple)
    
    print(result_list)
    print(result_tuple)