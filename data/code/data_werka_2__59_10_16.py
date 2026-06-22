def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_odd_list = [7, 14, 21, 28, 35]
    sample_even_list = [10, 20, 30, 40, 50, 60]
    
    try:
        print("Middle element of odd list:", find_middle_element(sample_odd_list))
    except ValueError as e:
        print(e)
    
    try:
        print("Middle element of even list:", find_middle_element(sample_even_list))
    except ValueError as e:
        print(e)