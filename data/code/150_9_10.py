def safe_remove_item(lst, item):
    while True:
        try:
            lst.remove(item)
        except ValueError:
            break

if __name__ == '__main__':
    sample_list = [1, 2, 'a', 3, 'b', 4, 'c']
    item_to_remove = 'b'
    safe_remove_item(sample_list, item_to_remove)
    print(sample_list)