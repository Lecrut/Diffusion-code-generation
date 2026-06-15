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
        "orange": 8,
        "grape": 12
    }
    sample_item_list = [
        "apple",
        "banana",
        "kiwi",
        "orange",
        "mango"
    ]
    filtered_items = filter_inventory(sample_inventory, sample_item_list)
    print(filtered_items)