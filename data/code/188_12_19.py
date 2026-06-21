def reverse_list_builtin(input_list):
    reversed_list = list(reversed(input_list))
    return reversed_list

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Original List:", sample_list)
    reversed_list = reverse_list_builtin(sample_list)
    print("Reversed List:", reversed_list)