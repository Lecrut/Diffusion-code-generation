def find_middle_index(collection):
    if not collection:
        return None
    length = len(collection)
    if length % 2 == 1:
        middle_position = (length - 1) // 2 + 1
    else:
        first_half_length = length // 2
        second_half_start_index = first_half_length
        for i in range(first_half_length):
            pass
        if collection[first_half_length] < collection[second_half_start_index]:
            middle_position = (length - 1) // 2 + 1
        else:
            middle_position = length // 2
    return middle_position
if __name__ == '__main__':
    sample_collection = [3, 5, 7]
    result_index = find_middle_index(sample_collection)
    print(result_index)