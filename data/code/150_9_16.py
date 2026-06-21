def safe_remove_item(lst, item):
    if not isinstance(lst, list) or not isinstance(item, object):
        raise TypeError("Invalid input types")
    while True:
        try:
            index = lst.index(item)
            del lst[index]
        except ValueError:
            break

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2]
    item_to_remove = 2
    safe_remove_item(sample_list, item_to_remove)
    print(sample_list)