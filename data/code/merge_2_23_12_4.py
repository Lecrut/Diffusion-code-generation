def create_inventory():
    return {
        "apple": {"quantity": 10, "price_per_unit": 0.5},
        "banana": {"quantity": 20, "price_per_unit": 0.3},
        "orange": {"quantity": 15, "price_per_unit": 0.4}
    }
def get_total_value(inventory):
    total = sum(item["quantity"] * item["price_per_unit"] for item in inventory.values())
    return round(total, 2)
if __name__ == '__main__':
    inv_data = create_inventory()
    print(f"Total Inventory Value: ${get_total_value(inv_data)}")