def find_middle_element(lst):
    return lst[(len(lst) - 1) // 2]

if __name__ == '__main__':
    sample_list_even = [10, 20, 30, 40]
    print(find_middle_element(sample_list_even))
    
    sample_list_odd = [5, 15, 25, 35, 45]
    print(find_middle_element(sample_list_odd))