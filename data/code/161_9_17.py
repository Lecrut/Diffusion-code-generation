def get_sorted_item_names():
    items = {
        'apple': 3,
        'banana': 2,
        'cherry': 5,
        'date': 4
    }
    sorted_items = sorted(items.keys())
    return sorted_items

if __name__ == '__main__':
    sample_items = {
        'elderberry': 6,
        'fig': 1,
        'grape': 7,
        'honeydew': 8,
        'kiwi': 9
    }
    sorted_sample_items = get_sorted_item_names()
    print(sorted_sample_items)