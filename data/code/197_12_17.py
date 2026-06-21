def validate_checklist_membership(checklist, items):
    return frozenset(items).issubset(frozenset(checklist))

if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry']
    items_to_check = ['banana', 'apple']
    print(validate_checklist_membership(checklist, items_to_check))