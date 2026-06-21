ITEMS = {
    "apple": 100,
    "banana": 150,
    "cherry": 200
}

def get_item_price(item_name):
    return ITEMS.get(item_name, None)

if __name__ == '__main__':
    print(get_item_price("apple"))
    print(get_item_price("banana"))
    print(get_item_price("grape"))