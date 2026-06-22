def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]

if __name__ == '__main__':
    sample_list_1 = [100, 200, 300]
    sample_list_2 = ['apple', 'banana']
    sample_list_3 = [True, False, True]
    
    result_1 = get_second_item(sample_list_1)
    result_2 = get_second_item(sample_list_2)
    result_3 = get_second_item(sample_list_3)
    
    print("Second item in sample_list_1:", result_1)
    print("Second item in sample_list_2:", result_2)
    print("Second item in sample_list_3:", result_3)