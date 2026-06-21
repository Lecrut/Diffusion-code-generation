def reverse_list_comprehension(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    
    return [item for item in reversed(input_list)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_comprehension(sample_list)
    print(reversed_list)