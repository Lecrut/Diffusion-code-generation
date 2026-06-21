def safe_remove_item(lst, item):
    while True:
        try:
            lst.remove(item)
        except ValueError:
            break

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    item_to_remove = 'banana'
    safe_remove_item(sample_list, item_to_remove)
    print(sample_list)