def reverse_list_builtin(input_list):
    return list(reversed(input_list))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_builtin(sample_list)
    print("Original List:", sample_list)
    print("-" * 30)
    print("Reversed List:", reversed_list)