def reverse_list(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    return reversed_list

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    print("Original list:", sample_list)
    reversed_list = reverse_list(sample_list)
    print("Reversed list (using manual insertion):", reversed_list)