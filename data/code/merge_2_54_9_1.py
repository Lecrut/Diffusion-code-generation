def get_middle_index(sequence):
    length = len(sequence)
    return (length - 1) // 2 if length % 2 == 0 else length // 2
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    middle_idx = get_middle_index(sample_list)
    print(middle_idx)