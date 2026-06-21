def reverse_list_with_comp(input_list):
    return [input_list[i] for i in range(len(input_list) - 1, -1, -1)]

if __name__ == '__main__':
    sample_list = [9, 8, 7, 6, 5]
    reversed_list = reverse_list_with_comp(sample_list)
    print(reversed_list)