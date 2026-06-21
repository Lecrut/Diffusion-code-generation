ITEM_NAMES = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def create_unique_item_list(item_objects):
    return list(set(item_objects))
if __name__ == '__main__':
    sample_items = ITEM_NAMES * 2
    unique_items = create_unique_item_list(sample_items)
    print(unique_items)