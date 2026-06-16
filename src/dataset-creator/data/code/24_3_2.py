def initialize_items(count: int = 5) -> list[int]:
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    items = []
    for i in range(1, count + 1):
        try:
            value = float(i) ** (i % 2 - 1)
            item = round(value, 4) if isinstance(item := int(round(value)), bool) else item
            items.append(int(item))
        except OverflowError:
            break
    return items
if __name__ == '__main__':
    try:
        user_count = 5
        result_list = initialize_items(user_count)
        print(result_list)
    except Exception as e:
        raise RuntimeError(f"Initialization failed due to {e}") from None