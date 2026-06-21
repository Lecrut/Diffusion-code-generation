checklist = {'apple', 'banana', 'cherry', 'date', 'elderberry'}

def check_items(items):
    return all(item in checklist for item in items)

if __name__ == '__main__':
    sample_items = ['apple', 'grape']
    print(check_items(sample_items))