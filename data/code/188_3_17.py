def reverse_list_comprehension(input_list):
    return [item for item in reversed(input_list)]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(reverse_list_comprehension(sample_values))