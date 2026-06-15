def reverse_list_slicing(input_list):
    return input_list[::-1]
def reverse_list_method(input_list):
    new_list = input_list[:]
    new_list.reverse()
    return new_list
def reverse_list_manual(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    return reversed_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original List:", sample_list)
    reversed_slicing = reverse_list_slicing(sample_list)
    print("Reversed (Slicing):", reversed_slicing)
    reversed_method = reverse_list_method(sample_list)
    print("Reversed (reverse()):", reversed_method)
    reversed_manual = reverse_list_manual(sample_list)
    print("Reversed (Manual):", reversed_manual)