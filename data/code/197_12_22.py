def validate_checklist_membership(checklist, items):
    if not isinstance(checklist, list) or not all(isinstance(item, str) for item in checklist):
        raise ValueError("Checklist must be a list of strings.")
    if not isinstance(items, (list, set)) or not all(isinstance(item, str) for item in items):
        raise ValueError("Items must be a list or set of strings.")
    
    checklist_set = frozenset(checklist)
    return all(item in checklist_set for item in items)

if __name__ == '__main__':
    sample_checklist = ['apple', 'banana', 'cherry']
    sample_items = {'banana', 'grape'}
    result = validate_checklist_membership(sample_checklist, sample_items)
    print("Checklist membership valid:", result)