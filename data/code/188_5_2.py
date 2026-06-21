def reverse_recursive(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        return [lst[0]]
    else:
        last = lst[-1]
        rest_reversed = reverse_recursive(lst[:-1])
        return [last] + rest_reversed

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original list:", sample_list)
    print("Reversed list:", reverse_recursive(sample_list))
    empty_list = []
    print("Original list:", empty_list)
    print("Reversed list:", reverse_recursive(empty_list))
    single_element_list = [7]
    print("Original list:", single_element_list)
    print("Reversed list:", reverse_recursive(single_element_list))