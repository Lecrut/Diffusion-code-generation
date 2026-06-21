def reverse_list_comprehension(input_list):
    return [item for item in reversed(input_list)]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    reversed_list = reverse_list_comprehension(sample_values)
    print(reversed_list)