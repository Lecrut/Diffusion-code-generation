def check_items(checklist, items):
    checklist_set = set(checklist)
    return all(item in checklist_set for item in items)

if __name__ == '__main__':
    sample_checklist = ['apple', 'banana', 'cherry']
    sample_items = ['banana', 'date']
    print(check_items(sample_checklist, sample_items))