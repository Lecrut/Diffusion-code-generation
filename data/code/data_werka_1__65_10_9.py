def get_sublist_by_index(lst):
    if not isinstance(lst, list) or len(lst) < 5:
        raise ValueError("Input must be a list with at least 5 elements.")
    return lst[2:5]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sublist = get_sublist_by_index(sample_list)
    print(sublist)