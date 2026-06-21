def get_center_item(seq):
    length = len(seq)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    center_index = length // 2
    return seq[center_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    center_value = get_center_item(sample_list)
    print(center_value)
    
    sample_tuple = (1, 2, 3)
    center_value_2 = get_center_item(sample_tuple)
    print(center_value_2)
    
    sample_string = "hello"
    center_value_3 = get_center_item(sample_string)
    print(center_value_3)