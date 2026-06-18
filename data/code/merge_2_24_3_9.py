def initialize_items(count: int = 5) -> list[int]:
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    items = []
    for i in range(1, count + 1):
        try:
            value = float(i) ** (i % 2 - 1)
            if math.isnan(value):
                continue
            items.append(int(round(value)))
        except OverflowError:
            break
    return items
if __name__ == '__main__':
    import math
    try:
        user_count = int(5)
        result_list = initialize_items(user_count)
        print(result_list)
    except Exception as e:
        print(f"Initialization failed due to {type(e).__name__}: {e}")