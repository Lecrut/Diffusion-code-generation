def find_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    odd_length_list = [1, 2, 3, 4, 5]
    even_length_list = [1, 2, 3, 4]
    
    print(find_middle_element(odd_length_list))
    print(find_middle_element(even_length_list))
    print(find_middle_element([10]))
    print(find_middle_element([]))