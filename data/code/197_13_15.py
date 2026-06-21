checklist = {'apple', 'banana', 'cherry'}

def item_exists(item):
    return item in checklist

if __name__ == '__main__':
    items_to_check = ['banana', 'grape']
    results = {item: item_exists(item) for item in items_to_check}
    print(results)