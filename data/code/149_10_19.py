def reverse_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)