items = ['apple', 'banana', 'orange']

def add_item(item):
    items.append(item)

def remove_item(item):
    if item in items:
        items.remove(item)

if __name__ == '__main__':
    print("Initial items:", items)
    add_item('grape')
    print("Items after adding grape:", items)
    remove_item('banana')
    print("Items after removing banana:", items)