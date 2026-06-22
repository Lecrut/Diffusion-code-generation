def reverse_list(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    return reversed_list

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Original list:", sample_list)
    reversed_list = reverse_list(sample_list)
    print("Reversed list (using insertion):", reversed_list)

    sample_list_2 = ['a', 'b', 'c', 'd']
    print("\nOriginal list:", sample_list_2)
    reversed_list_2 = reverse_list(sample_list_2)
    print("Reversed list (using insertion):", reversed_list_2)