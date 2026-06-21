import bisect

def insert_sorted(item_list, item):
    bisect.insort(item_list, item)
    return item_list

if __name__ == '__main__':
    items = ['apple', 'banana', 'cherry']
    new_item = 'date'
    updated_items = insert_sorted(items, new_item)
    print(updated_items)