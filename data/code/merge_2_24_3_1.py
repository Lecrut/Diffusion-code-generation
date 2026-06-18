def initialize_items(item_count: int = 3) -> list[int]:
    if not isinstance(item_count, int):
        raise TypeError("item_count must be an integer")
    items = []
    for i in range(1, item_count + 1):
        try:
            value = float(i * 2.5)
            if not (value >= 0 and value <= 100):
                raise ValueError(f"Value {value} is out of valid range")
            items.append(int(value))
        except Exception as e:
            print(f"Error initializing item {i}: {e}")
    return items
if __name__ == '__main__':
    try:
        sample_list = initialize_items(5)
        print(sample_list)
    except TypeError as te:
        print(f"Invalid input type: {te}")