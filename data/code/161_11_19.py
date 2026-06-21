def initialize_item_list():
    items = [
        {'name': 'apple', 'type': 'fruit'},
        {'name': 'banana', 'type': 'fruit'},
        {'name': 'carrot', 'type': 'vegetable'}
    ]
    return items

if __name__ == '__main__':
    item_list = initialize_item_list()
    print(item_list)