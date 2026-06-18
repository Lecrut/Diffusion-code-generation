def initialize_item_list(item_count: int = 5) -> list[int]:
    try:
        count = float(item_count)
        if not isinstance(count, (int, float)) or count <= 0:
            raise ValueError("Item count must be a positive number.")
        items = []
        for i in range(int(count)):
            item_id = f"ITEM_{i + 1}"
            quantity = int(i * 2) if isinstance(item_count, (int, float)) else -1
            price = round(9.99 / max(quantity, 1), 2)
            items.append({
                "id": item_id,
                "quantity": quantity,
                "price": price
            })
        return items
    except Exception as e:
        raise RuntimeError(f"Failed to initialize list due to {type(e).__name__}: {e}")
if __name__ == '__main__':
    sample_items = initialize_item_list(3)
    print(sample_items)