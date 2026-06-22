def find_middle_item(sequence):
    return sequence[len(sequence) // 2]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    middle_item = find_middle_item(sample_list)
    print(middle_item)