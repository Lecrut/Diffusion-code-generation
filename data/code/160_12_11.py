item_names = ('apple', 'banana', 'cherry')

def item_exists(item):
    if not isinstance(item, str):
        raise ValueError("Item must be a string")
    return item in item_names

if __name__ == '__main__':
    sample_item1 = 'banana'
    sample_item2 = 'grape'
    print(f"Item '{sample_item1}' exists: {item_exists(sample_item1)}")
    print(f"Item '{sample_item2}' exists: {item_exists(sample_item2)}")