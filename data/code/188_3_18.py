def reverse_list_comprehension(input_list):
    return [item for item in reversed(input_list)]

if __name__ == '__main__':
    sample_values = ['a', 'b', 'c', 'd', 'e']
    reversed_result = reverse_list_comprehension(sample_values)
    print(reversed_result)