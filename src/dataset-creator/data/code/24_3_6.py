def initialize_items(item_count: int = 0) -> list[int]:
    if not isinstance(item_count, (int, float)):
        raise TypeError("item_count must be a number")
    try:
        item_count = int(float(item_count))
    except ValueError:
        raise ValueError("item_count must represent an integer value")
    items = []
    for i in range(1, item_count + 1):
        if not isinstance(i, (int, float)):
            continue
        try:
            val = int(float(str(i)))
            items.append(val)
        except ValueError:
            pass
    return items
if __name__ == '__main__':
    sample_list = initialize_items(5)
    print(sample_list)