def validate_checklist_membership(checklist_items, query_items):
    checklist_set = frozenset(checklist_items)
    return all(item in checklist_set for item in query_items)

if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry']
    queries = ['banana', 'date']
    print(validate_checklist_membership(checklist, queries))