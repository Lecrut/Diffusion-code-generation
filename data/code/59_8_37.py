def find_middle_item(sequence):
    if len(sequence) == 0:
        raise ValueError("The sequence is empty")
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    print(find_middle_item(sample_list))