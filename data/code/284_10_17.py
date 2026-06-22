def reverse_list_method(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    return reversed_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original list:", sample_list)
    reversed_list = reverse_list_method(sample_list)
    print("Reversed list (using method):", reversed_list)

    sample_list_2 = ['a', 'b', 'c', 'd']
    print("\nOriginal list:", sample_list_2)
    reversed_list_2 = reverse_list_method(sample_list_2)
    print("Reversed list (using method):", reversed_list_2)

    sample_list_3 = [10, 20, 30, 40]
    print("\nOriginal list:", sample_list_3)
    reversed_list_3 = reverse_list_method(sample_list_3)
    print("Reversed list (using method):", reversed_list_3)