def reverse_recursive(lst):
    if not lst:
        return []
    else:
        last = lst[-1]
        rest_reversed = reverse_recursive(lst[:-1])
        return [last] + rest_reversed

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Original list:", sample_list)
    print("Reversed list:", reverse_recursive(sample_list))
    
    single_element_list = [7]
    print("Original list:", single_element_list)
    print("Reversed list:", reverse_recursive(single_element_list))
    
    empty_list = []
    print("Original list:", empty_list)
    print("Reversed list:", reverse_recursive(empty_list))