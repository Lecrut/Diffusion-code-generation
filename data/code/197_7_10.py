def check_items(checklist, items):
    return set(items).intersection(checklist)

if __name__ == '__main__':
    checklist = {'apple', 'banana', 'cherry'}
    items = ['banana', 'date']
    print(check_items(checklist, items))