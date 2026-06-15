def filter_inventory(inventory, item_list):
    result = {}
    for item in item_list:
        if item in inventory:
            result[item] = inventory[item]
    return result
if __name__ == '__main__':
    sample_inventory = {
        "apple": 10,
        "banana": 5,
        "orange": 12,
        "grape": 8
    }
    sample_item_names = [
        "apple",
        "banana",
        "mango",
        "orange",
        "kiwi"
    ]
    filtered_items = filter_inventory(sample_inventory, sample_item_names)
    print(filtered_items)