MIDDLE_INDEX = (len(lst) - 1) // 2

def find_middle_element(lst):
    return lst[MIDDLE_INDEX]

if __name__ == '__main__':
    sample_list_odd = [100, 200, 300]
    print(find_middle_element(sample_list_odd))
    
    sample_list_even = [1, 2, 3, 4]
    print(find_middle_element(sample_list_even))