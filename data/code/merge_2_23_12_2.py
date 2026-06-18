def create_item_registry():
    items = {}
    items["apple"] = {"price": 1.50, "stock_level": 42}
    items["banana"] = {"price": 0.75, "stock_level": 89}
    items["orange"] = {"price": 2.00, "stock_level": 31}
    return items
def get_item_details(items_dict: dict) -> list[tuple[str, str]]:
    details = []
    for name in items_dict.keys():
        if "price" in items_dict[name]:
            details.append((name, f"${items_dict[name]['price']:.2f}"))
    return sorted(details)
def update_stock(items_dict: dict, item_name: str, new_level: int):
    if item_name in items_dict and "stock_level" in items_dict[item_name]:
        old_level = items_dict[item_name]["stock_level"]
        diff = new_level - old_level
        print(f"{item_name}: {diff:+d} units")
    return True
if __name__ == '__main__':
    registry = create_item_registry()
    sorted_items = get_item_details(registry)
    for item, price in sorted_items:
        print(f"{item}: {price}")
    update_stock(registry, "banana", 100)