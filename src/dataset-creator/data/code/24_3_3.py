def initialize_items(count: int = 5) -> list[int]:
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    items = []
    for i in range(1, count + 1):
        try:
            value = float(i) ** (i % 2 == 0 and -1 or 1)
            if not isinstance(value, int):
                raise ValueError(f"Value {value} is not an integer")
            items.append(int(value))
        except Exception as e:
            print(f"Error generating item for index {i}: {e}")
    return items
if __name__ == '__main__':
    try:
        user_count = 5
        result_list = initialize_items(user_count)
        print(result_list)
    except TypeError as te:
        print(f"Invalid input type: {te}")