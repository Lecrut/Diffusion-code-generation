def reverse_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e']
    reversed_list = reverse_list(sample_list)
    print(reversed_list)