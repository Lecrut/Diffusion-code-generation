def validate_checklist_membership(checklist, items):
    checklist_set = frozenset(checklist)
    return all((item in checklist_set for item in items))
if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry']
    items_to_check = ['banana', 'grape']
    result = validate_checklist_membership(checklist, items_to_check)
    print(result)