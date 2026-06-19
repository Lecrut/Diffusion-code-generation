def find_middle_item(data):
    length = len(data)
    middle_index = (length - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list_odd = [7, 14, 21, 28, 35]
    sample_list_even = [10, 20, 30, 40, 50, 60]
    single_element_list = [42]
    
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))
    print(find_middle_item(single_element_list))