def contains_item(collection, item):
    return item in collection

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry', 'date']
    target_item = 'banana'
    if contains_item(sample_items, target_item):
        print(f"The item '{target_item}' exists in the list.")
    else:
        print(f"The item '{target_item}' does not exist in the list.")