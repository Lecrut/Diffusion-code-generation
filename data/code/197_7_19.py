def check_items(checklist, items):
    return set(items).intersection(set(checklist))

if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry']
    items_to_check = ['banana', 'date', 'elderberry']
    matching_items = check_items(checklist, items_to_check)
    print(matching_items)