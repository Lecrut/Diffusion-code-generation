def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    first_sequence = [7, 8, 9]
    second_sequence = [10, 11, 12]
    result_sequence = concatenate_lists(first_sequence, second_sequence)
    print(result_sequence)