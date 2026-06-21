CHECKLIST = {
    'group_a': {'apple', 'banana', 'cherry'},
    'group_b': {'banana', 'date', 'elderberry'},
    'group_c': {'fig', 'grape', 'apple'}
}

def check_membership(item, checklist=CHECKLIST):
    return any(item in group for group in checklist.values())

if __name__ == '__main__':
    items_to_check = ['apple', 'orange', 'banana']
    results = {item: check_membership(item) for item in items_to_check}
    print(results)