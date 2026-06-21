def reverse_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    sample_values = [7, 6, 5, 4, 3, 2, 1]
    reversed_values = reverse_list(sample_values)
    print(reversed_values)