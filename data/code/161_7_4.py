item_prices = {
    "apple": 100,
    "banana": 150,
    "cherry": 200
}

def get_item_price(item):
    return item_prices.get(item, None)

if __name__ == '__main__':
    print(f"Price of apple: {get_item_price('apple')}")
    print(f"Price of banana: {get_item_price('banana')}")
    print(f"Price of grape: {get_item_price('grape')}")