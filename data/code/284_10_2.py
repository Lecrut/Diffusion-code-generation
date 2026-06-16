import sys
def reverse_list_slicing(input_list):
    return input_list[::-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Original List:", sample_list)
    reversed_list = reverse_list_slicing(sample_list)
    print("Reversed List (using slicing):", reversed_list)