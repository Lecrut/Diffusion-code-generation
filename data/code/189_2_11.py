def remove_item_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    else:
        raise IndexError('Index out of bounds')
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        remove_item_by_index(sample_list, 2)
        print(sample_list)
    except IndexError as e:
        print(e)
    try:
        remove_item_by_index(sample_list, 5)
    except IndexError as e:
        print(e)