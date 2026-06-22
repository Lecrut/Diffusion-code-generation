def get_middle_element(seq):
    length = len(seq)
    if length == 0:
        return None
    mid_index = (length - 1) // 2
    return seq[mid_index]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [10, 20, 30, 40]
    empty_list = []
    single_list = [42]
    
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
    print(get_middle_element(empty_list))
    print(get_middle_element(single_list))