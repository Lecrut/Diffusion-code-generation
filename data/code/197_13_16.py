checklist = {
    'apple': True,
    'banana': True,
    'cherry': False,
    'date': True,
    'elderberry': False
}

def check_items(items):
    items_set = set(items)
    return {item: item in checklist for item in items}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'fig', 'date']
    results = check_items(sample_items)
    print(results)