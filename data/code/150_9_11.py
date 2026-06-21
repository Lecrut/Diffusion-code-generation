def safe_remove_item(lst, item):
    try:
        while True:
            index = lst.index(item)
            del lst[index]
    except ValueError:
        return

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    item_to_remove = 3
    safe_remove_item(sample_list, item_to_remove)
    print(sample_list)