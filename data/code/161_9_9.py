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
        'elderberry': 1,
        'fig': 6,
        'grape': 3,
        'honeydew': 2
    }
    sorted_sample = get_sorted_item_names()
    print(sorted_sample)