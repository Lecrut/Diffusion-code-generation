def validate_checklist_membership(checklist_items, query_items):
    checklist_set = frozenset(checklist_items)
    return all(item in checklist_set for item in query_items)

if __name__ == '__main__':
    sample_checklist = ['apple', 'banana', 'cherry']
    sample_query = ['banana', 'date']
    print(validate_checklist_membership(sample_checklist, sample_query))