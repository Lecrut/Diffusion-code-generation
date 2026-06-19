def reverse_list_by_index_manipulation(input_list):
    length = len(input_list)
    midpoint = length // 2
    for i in range(midpoint):
        left_index = i
        right_index = length - 1 - i
        temp = input_list[left_index]
        input_list[left_index] = input_list[right_index]
        input_list[right_index] = temp
    return input_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6]
    reversed_list = reverse_list_by_index_manipulation(sample_list)
    print(reversed_list)