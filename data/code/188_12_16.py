def reverse_list(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    
    return list(reversed(input_list))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original List:", sample_list)
    reversed_list = reverse_list(sample_list)
    print("Reversed List:", reversed_list)