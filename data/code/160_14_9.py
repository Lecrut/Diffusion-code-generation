def filter_items_by_initial(items, initial):
    if not items or not isinstance(initial, str) or len(initial) != 1:
        raise ValueError("Invalid input: 'items' must be a non-empty list and 'initial' must be a single character.")
    
    return [item for item in items if item.startswith(initial)]

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    filtered_items = filter_items_by_initial(sample_items, 'a')
    print(filtered_items)