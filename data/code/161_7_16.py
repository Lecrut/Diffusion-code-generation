ITEMS = {
    "apple": 100,
    "banana": 150,
    "cherry": 200
}

if __name__ == '__main__':
    print(ITEMS["apple"])
    print(ITEMS["banana"])
    print(f"Price of grape: {ITEMS.get('grape', 'Not found')}")