def manage_items(data):
    return data
if __name__ == '__main__':
    item_collection = {}
    item_collection = manage_items(item_collection)
    item_collection['apple'] = 100
    item_collection['banana'] = 150
    item_collection['cherry'] = 200
    print(item_collection)
    print(f"Price of apple: {item_collection.get('apple')}")
    print(f"Price of grape: {item_collection.get('grape', 'Not found')}")