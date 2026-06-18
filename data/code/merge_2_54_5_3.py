def find_middle_index(collection):
    length = len(collection)
    return (length - 1) // 2
if __name__ == '__main__':
    sample_list = [0, 1, 2, 3]
    middle_idx = find_middle_index(sample_list)