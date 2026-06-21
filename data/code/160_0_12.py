def manage_item_list(items):
    item_set = set(items)

    def add_item(item):
        if item not in item_set:
            item_set.add(item)
        else:
            raise ValueError(f"Item '{item}' already exists.")

    def remove_item(item):
        if item in item_set:
            item_set.remove(item)
        else:
            raise ValueError(f"Item '{item}' does not exist.")

    return add_item, remove_item

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'orange']
    add_item, remove_item = manage_item_list(sample_items)

    try:
        add_item('grape')
        print("Grape added successfully.")
    except ValueError as e:
        print(e)

    try:
        add_item('apple')
    except ValueError as e:
        print(e)

    try:
        remove_item('banana')
        print("Banana removed successfully.")
    except ValueError as e:
        print(e)

    try:
        remove_item('mango')
    except ValueError as e:
        print(e)