def filter_items_by_initial(items, initial):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All items must be strings")
    if not isinstance(initial, str) or len(initial) != 1:
        raise ValueError("Initial must be a single character string")
    
    return [item for item in items if item.startswith(initial)]

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    filtered_items = filter_items_by_initial(sample_items, 'a')
    print(filtered_items)