def reverse_list_comprehension(input_list):
    return [item for item in input_list[::-1]]

if __name__ == '__main__':
    sample_values = ['a', 'b', 'c', 'd']
    reversed_list = reverse_list_comprehension(sample_values)
    print(reversed_list)