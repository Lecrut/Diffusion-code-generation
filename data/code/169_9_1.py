def calculate_inventory_value(inventory, prices):
    total_value = 0
    for item, quantity in inventory.items():
        if item in prices:
            total_value += quantity * prices[item]
    return total_value
if __name__ == '__main__':
    inventory_data = {
        "apple": 10,
        "banana": 5,
        "orange": 8
    }
    price_data = {
        "apple": 0.50,
        "banana": 0.30,
        "orange": 0.60,
        "grape": 1.50
    }
    total = calculate_inventory_value(inventory_data, price_data)
    print(total)