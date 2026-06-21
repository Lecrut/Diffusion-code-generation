checklist = {'apple', 'banana', 'cherry'}

def items_in_checklist(items):
    return set(items) & checklist

if __name__ == '__main__':
    sample_items = ['apple', 'orange', 'banana']
    print(items_in_checklist(sample_items))