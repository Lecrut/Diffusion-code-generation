checklist = {'apple', 'banana', 'cherry'}

def check_items(items):
    return items.intersection(checklist)

if __name__ == '__main__':
    sample_items = {'banana', 'grape'}
    print(check_items(sample_items))