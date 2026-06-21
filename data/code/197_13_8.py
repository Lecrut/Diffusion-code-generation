checklist = {'apple': True, 'banana': False, 'cherry': True, 'date': True, 'elderberry': False}

def check_items(items):
    missing_items = [item for item in items if checklist.get(item, False) is not True]
    return missing_items
if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry', 'fig']
    result = check_items(sample_items)
    print(result)