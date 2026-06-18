def initialize_items(quantity: int = 0) -> list[int]:
    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer.")
    items = []
    for i in range(1, quantity + 1):
        item_id = f"Item_{i}"
        price = float(i * 9.99)
        items.append({"id": item_id, "price": round(price, 2)})
    return items
if __name__ == '__main__':
    try:
        user_quantity = int(5)
        result_list = initialize_items(user_quantity)
        print(result_list)
    except ValueError as ve:
        print(f"Input error: {ve}")