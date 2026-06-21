def create_item_list():
    item_types = ["fruit", "number"]
    items = []
    for i in range(10):
        item_type = item_types[i % 2]
        if item_type == "fruit":
            items.append({"id": i + 1, "type": "fruit", "name": f"Fruit {i + 1}"})
        else:
            items.append({"id": i + 1, "type": "number", "value": i * 10})
    return items

if __name__ == '__main__':
    item_list = create_item_list()
    for index, item in enumerate(item_list):
        print(f"{index + 1}. ID: {item['id']}, Type: {item['type']}, Value: {item['value']}")