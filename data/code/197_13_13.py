def check_items(checklist, items):
    checklist_set = set(checklist)
    return all(item in checklist_set for item in items)

if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry']
    items_to_check = ['banana', 'orange']
    print(check_items(checklist, items_to_check))