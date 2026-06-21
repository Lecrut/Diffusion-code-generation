def safe_remove_item(lst, item):
    while True:
        try:
            lst.remove(item)
        except ValueError:
            break

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item_to_remove = 3
    safe_remove_item(sample_list, item_to_remove)
    print(sample_list)