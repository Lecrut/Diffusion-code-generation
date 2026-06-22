def reverse_list(input_list):
    reversed_list = input_list[::-1]
    return reversed_list

if __name__ == '__main__':
    sample_values = [5, 4, 3, 2, 1]
    result = reverse_list(sample_values)
    print(result)