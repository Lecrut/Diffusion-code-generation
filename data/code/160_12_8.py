item_names = ('apple', 'banana', 'cherry')

def item_exists(item):
    return item in item_names

if __name__ == '__main__':
    sample_item1 = 'banana'
    sample_item2 = 'grape'
    result1 = item_exists(sample_item1)
    result2 = item_exists(sample_item2)
    print(f"Item '{sample_item1}' exists: {result1}")
    print(f"Item '{sample_item2}' exists: {result2}")