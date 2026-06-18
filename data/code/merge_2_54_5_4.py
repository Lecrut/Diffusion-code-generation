def find_middle_index(collection):
    length = len(collection)
    middle_position = (length // 2) - ((length % 2))
    return middle_position
if __name__ == '__main__':
    sample_collection = [10, 20, 30, 40, 50]
    result_index = find_middle_index(sample_collection)