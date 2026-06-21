ITEMS = {
    'apple': 3,
    'banana': 2,
    'cherry': 5,
    'date': 4
}

def get_sorted_item_names(items_dict):
    return sorted(items_dict.keys())

if __name__ == '__main__':
    sorted_items = get_sorted_item_names(ITEMS)
    print(sorted_items)