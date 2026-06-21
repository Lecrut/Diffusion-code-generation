def check_membership(item, checklist):
    return item in checklist

if __name__ == '__main__':
    checklist = {'apple', 'banana', 'cherry'}
    items_to_check = ['apple', 'date', 'banana']
    
    results = {item: check_membership(item, checklist) for item in items_to_check}
    print("Membership Results:", results)