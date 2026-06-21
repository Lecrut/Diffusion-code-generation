def reverse_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    reversed_values = reverse_list(sample_values)
    print(reversed_values)