def validate_index_range(lst, start, end):
    if not (0 <= start < len(lst)) or not (0 <= end <= len(lst)):
        raise IndexError("Index out of bounds")

def get_sublist_by_position(lst, start, end):
    validate_index_range(lst, start, end)
    return lst[start:end]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result_sublist = get_sublist_by_position(sample_list, 2, 5)
    print(result_sublist)