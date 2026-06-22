def get_middle_element(seq):
    length = len(seq)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    middle_index = (length - 1) // 2
    return seq[middle_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    
    odd_result = get_middle_element(odd_list)
    even_result = get_middle_element(even_list)
    
    print(odd_result)
    print(even_result)