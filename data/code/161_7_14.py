ITEMS = {
    "apple": 100,
    "banana": 150,
    "cherry": 200
}

def get_item_price(item_name):
    return ITEMS.get(item_name, "Item not found")

if __name__ == '__main__':
    print(f"Price of apple: {get_item_price('apple')}")
    print(f"Price of grape: {get_item_price('grape')}")