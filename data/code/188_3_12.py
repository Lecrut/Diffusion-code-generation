def reverse_list_comprehension(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    return [input_list[i] for i in range(len(input_list) - 1, -1, -1)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_comprehension(sample_list)
    print(reversed_list)