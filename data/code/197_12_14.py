def validate_checklist_membership(checklist, items):
    return frozenset(items).issubset(frozenset(checklist))
if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry']
    items = ['banana', 'apple']
    print(validate_checklist_membership(checklist, items))