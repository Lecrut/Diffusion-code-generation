if __name__ == '__main__':
    item_data = {}
    item_data["Apple"] = ("Apple", "A sweet red fruit.")
    item_data["Banana"] = ("Banana", "A long yellow fruit.")
    item_data["Carrot"] = ("Carrot", "An orange root vegetable.")
    item_data["Milk"] = ("Milk", "A white dairy product.")
    for item, data in item_data.items():
        name, description = data
        print(f"Item: {name}, Description: {description}")