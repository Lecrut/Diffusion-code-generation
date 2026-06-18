def create_item_list():
    item_list = [
        {'name': 'Apple', 'price': 0.50},
        {'name': 'Banana', 'price': 0.30},
        {'name': 'Orange', 'price': 0.75}
    ]
    return item_list
if __name__ == '__main__':
    my_list = create_item_list()
    print(my_list)