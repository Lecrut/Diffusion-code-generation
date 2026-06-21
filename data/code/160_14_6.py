items = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']

def filter_items_by_initial(items, initial):
    return [item for item in items if item.startswith(initial)]

if __name__ == '__main__':
    filtered_items = filter_items_by_initial(items, 'a')
    print(filtered_items)