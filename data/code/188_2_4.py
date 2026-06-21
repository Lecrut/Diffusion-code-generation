def reverse_using_iter(input_list):
    return list(reversed(input_list))

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    reversed_values = reverse_using_iter(sample_values)
    print(reversed_values)