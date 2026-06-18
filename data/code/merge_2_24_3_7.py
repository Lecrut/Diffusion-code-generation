def initialize_items(count: int = 0) -> list[int]:
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    items = []
    for i in range(1, count + 1):
        try:
            value = float(i * 2.5)
            if not (value > -30 and value < 40):
                continue
            item_type = "sensor" if abs(value) < 15 else "actuator"
            items.append({
                "id": i,
                "type": item_type,
                "status": "active",
                "value": round(value, 2)
            })
        except (ValueError, TypeError):
            continue
    return items
if __name__ == '__main__':
    sample_count = 10
    try:
        item_list = initialize_items(sample_count)
        for idx, item in enumerate(item_list, start=1):
            print(f"Item {idx}: ID={item['id']}, Type={item['type'].upper()}, Value={item['value']}")
    except Exception as e:
        print(f"Initialization failed due to error: {e}")