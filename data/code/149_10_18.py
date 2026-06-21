def reverse_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    if not isinstance(sample_list, list) or not all(isinstance(item, int) for item in sample_list):
        raise ValueError("Input must be a list of integers")
    
    reversed_list = reverse_list(sample_list)
    print(reversed_list)