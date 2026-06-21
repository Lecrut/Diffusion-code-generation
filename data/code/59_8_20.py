def find_middle_item(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("The sequence is empty")
    middle_index = length // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(find_middle_item(sample_list))