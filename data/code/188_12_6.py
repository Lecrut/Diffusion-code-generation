def reverse_list_builtin(input_list):
    return list(reversed(input_list))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original List:", sample_list)
    reversed_list = reverse_list_builtin(sample_list)
    print("Reversed (Builtin):", reversed_list)