def reverse_list_slicing(data):
    return data[::-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_slicing(sample_list)
    print(reversed_list)