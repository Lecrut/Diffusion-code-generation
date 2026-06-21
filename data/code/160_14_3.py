def filter_items_by_initial(items, initial):
    return [item for item in items if item.startswith(initial)]

if __name__ == '__main__':
    sample_items = ['grape', 'kiwi', 'avocado', 'apple', 'apricot']
    filtered_items = filter_items_by_initial(sample_items, 'a')
    print(filtered_items)