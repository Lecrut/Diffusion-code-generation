def get_sorted_item_names():
    items = {
        'apple': 3,
        'banana': 2,
        'cherry': 5,
        'date': 4
    }
    return sorted(items.keys())

if __name__ == '__main__':
    print(get_sorted_item_names())