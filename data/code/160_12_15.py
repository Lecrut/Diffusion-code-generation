item_names = ('apple', 'banana', 'cherry')

def item_exists(item):
    if not isinstance(item, str):
        raise ValueError("Item must be a string")
    return item in item_names

if __name__ == '__main__':
    print(f"Item 'banana' exists: {item_exists('banana')}")
    print(f"Item 'grape' exists: {item_exists('grape')}")