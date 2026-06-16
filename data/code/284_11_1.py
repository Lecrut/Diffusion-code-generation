def reverse_list(input_list):
    return input_list[::-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)
    sample_list_2 = ['a', 'b', 'c', 'd']
    reversed_list_2 = reverse_list(sample_list_2)
    print(reversed_list_2)