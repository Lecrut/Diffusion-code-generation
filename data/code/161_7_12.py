ITEMS = {
    "apple": 100,
    "banana": 150,
    "cherry": 200
}

if __name__ == '__main__':
    print(f"Price of apple: {ITEMS.get('apple')}")
    print(f"Price of grape: {ITEMS.get('grape', 'Not found')}")