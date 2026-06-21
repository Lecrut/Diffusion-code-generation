def reverse_list_comprehension(input_list):
    return [item for item in reversed(input_list)]

if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    reversed_result = reverse_list_comprehension(sample_list)
    print(reversed_result)