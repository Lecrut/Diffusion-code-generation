def filter_items_by_initial(items, initial):
    if not all((isinstance(item, str) for item in items)):
        raise ValueError("All elements in 'items' must be strings.")
    if not isinstance(initial, str) or len(initial) != 1:
        raise ValueError("'initial' must be a single character string.")
    return [item for item in items if item.startswith(initial)]
if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    initial_char = 'a'
    filtered_items = filter_items_by_initial(sample_items, initial_char)
    print(filtered_items)