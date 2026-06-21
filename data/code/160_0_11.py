items = ['apple', 'banana', 'orange']

def add_item(item):
    items.append(item)

def remove_item(item):
    if item in items:
        items.remove(item)

if __name__ == '__main__':
    add_item('grape')
    remove_item('banana')
    print(items)