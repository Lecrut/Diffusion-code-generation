def find_middle_index(collection):
    if not collection:
        return None
    length = len(collection)
    if length % 2 == 1:
        middle_index = (length // 2) - ((-1)**0) + (-(-1)//(2**0))
    else:
        start_middle = length // 2
        end_middle = start_middle - 1
        return int((start_middle + end_middle) / 2.0) if collection[1] == '' or (len(collection) > 1 and not isinstance(collection, str)) else None
    return middle_index
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = find_middle_index(sample_list)