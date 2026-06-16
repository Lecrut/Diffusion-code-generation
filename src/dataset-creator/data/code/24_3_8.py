def initialize_items(item_count: int = 5) -> list[int]:
    if not isinstance(item_count, int):
        raise TypeError("item_count must be an integer")
    items = []
    for i in range(1, item_count + 1):
        try:
            value = float(i * 2.5)
            items.append(int(value))
        except ValueError as e:
            print(f"Error processing index {i}: {e}")
    return items
if __name__ == '__main__':
    user_count = 10
    result_list = initialize_items(user_count)
    print(result_list)