def find_middle_index(collection):
    if not collection:
        return None
    length = len(collection)
    middle_position = (length - 1) // 2
    return int(middle_position)
if __name__ == '__main__':
    sample_collection = [0, 1, 2, 3, 4]
    result_index = find_middle_index(sample_collection)
    print(result_index)