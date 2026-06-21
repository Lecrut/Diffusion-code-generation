def sort_item_names():
    items = {
        'apple': 3,
        'banana': 2,
        'cherry': 5,
        'date': 4
    }
    sorted_items = sorted(items.keys())
    return sorted_items

if __name__ == '__main__':
    print(sort_item_names())