def reverse_list_with_concat(input_list):
    reversed_iterator = reversed(input_list)
    reversed_list = []
    for item in reversed_iterator:
        reversed_list.append(item)
    return reversed_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_result = reverse_list_with_concat(sample_list)
    print(reversed_result)