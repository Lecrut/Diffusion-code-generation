item_names = ('apple', 'banana', 'cherry')

def item_exists(item):
    return item in item_names

if __name__ == '__main__':
    sample_item1 = 'banana'
    sample_item2 = 'orange'
    print(f"Item '{sample_item1}' exists: {item_exists(sample_item1)}")
    print(f"Item '{sample_item2}' exists: {item_exists(sample_item2)}")