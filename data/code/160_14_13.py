def filter_items_by_initial(items, initial):
    filtered_items = []
    for item in items:
        if item.startswith(initial):
            filtered_items.append(item)
    return filtered_items

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    filtered_items = filter_items_by_initial(sample_items, 'a')
    print(filtered_items)