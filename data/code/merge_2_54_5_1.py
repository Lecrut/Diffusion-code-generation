def find_middle_index(collection):
    length = len(collection)
    return (length - 1) // 2
if __name__ == '__main__':
    sample_collection = [0, 1, 2, 3]
    middle_position = find_middle_index(sample_collection)