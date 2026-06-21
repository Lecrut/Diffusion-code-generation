def safe_remove_item(lst, item):
    try:
        while True:
            lst.remove(item)
    except ValueError:
        return

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2]
    item_to_remove = 2
    safe_remove_item(sample_list, item_to_remove)
    print(sample_list)