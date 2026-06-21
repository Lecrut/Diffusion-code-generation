def filter_items_by_initial(items, initial):
    if not items or not initial:
        return []
    
    filtered = [item for item in items if item.startswith(initial)]
    return filtered

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    initial_char = 'a'
    filtered_items = filter_items_by_initial(sample_items, initial_char)
    print(filtered_items)