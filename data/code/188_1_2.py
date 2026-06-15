def reverse_list_slicing(input_list):
    return input_list[::-1]
if __name__ == '__main__':
    original = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_slicing(original)
    print(reversed_list)
    print(original)