CHECKLIST_MEMBERSHIP = 'checklist_membership'

def convert_to_frozenset(items):
    return frozenset(items)

def validate_membership(checklist_set, items):
    return all(item in checklist_set for item in items)

if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry']
    items_to_check = ['banana', 'grape']
    
    checklist_set = convert_to_frozenset(checklist)
    result = validate_membership(checklist_set, items_to_check)
    
    print(result)