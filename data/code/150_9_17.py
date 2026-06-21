def safe_remove_item(lst, item):
    while True:
        try:
            index = lst.index(item)
            del lst[index]
        except ValueError:
            break

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    item_to_remove = 50
    safe_remove_item(sample_list, item_to_remove)
    print(sample_list)