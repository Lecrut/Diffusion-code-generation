def reverse_recursive(lst):
    if not lst:
        return []
    else:
        return [lst[-1]] + reverse_recursive(lst[:-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Reversed list:", reverse_recursive(sample_list))
    empty_list = []
    print("Reversed list:", reverse_recursive(empty_list))
    single_element_list = [7]
    print("Reversed list:", reverse_recursive(single_element_list))