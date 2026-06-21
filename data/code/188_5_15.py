def reverse_recursive(lst):
    if not isinstance(lst, list) or not all(isinstance(x, (int, str)) for x in lst):
        raise ValueError("Input must be a list of integers and/or strings")
    if len(lst) <= 1:
        return lst
    else:
        return [lst[-1]] + reverse_recursive(lst[:-1])

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