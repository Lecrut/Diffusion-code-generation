def find_last_occurrence(lst, item):
    try:
        return lst.rindex(item)
    except ValueError:
        return -1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    item_to_find = 2
    index = find_last_occurrence(sample_list, item_to_find)
    print(index)