def validate_checklist_membership(checklist, items):
    checklist_set = frozenset(checklist)
    return all(item in checklist_set for item in items)

if __name__ == '__main__':
    sample_checklist = ['apple', 'banana', 'cherry']
    sample_items = ['banana', 'cherry', 'date']
    print(validate_checklist_membership(sample_checklist, sample_items))