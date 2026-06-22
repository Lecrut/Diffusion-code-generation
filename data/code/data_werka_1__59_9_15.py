def find_middle_item(sequence):
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(find_middle_item(sample_list))