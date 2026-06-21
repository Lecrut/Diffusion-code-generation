def check_items_against_checklist(items_to_check, checklist):
    items_set = set(items_to_check)
    checklist_set = set(checklist)
    return items_set.intersection(checklist_set)

if __name__ == '__main__':
    items_to_check = ['banana', 'grape', 'apple']
    checklist = ['apple', 'banana', 'cherry', 'fig']
    result = check_items_against_checklist(items_to_check, checklist)
    print("Common Items:", result)