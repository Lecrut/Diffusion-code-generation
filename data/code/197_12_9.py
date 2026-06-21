def validate_checklist_membership(checklist, items):
    if not isinstance(checklist, list) or not all(isinstance(item, str) for item in checklist):
        raise ValueError("Checklist must be a list of strings")
    if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
        raise ValueError("Items must be a list of strings")

    checklist_set = frozenset(checklist)
    return all(item in checklist_set for item in items)

if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry']
    items_to_check = ['banana', 'grape']
    print(validate_checklist_membership(checklist, items_to_check))