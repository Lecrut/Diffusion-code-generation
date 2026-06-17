def update_dictionary(data: dict, new_items: list[tuple]) -> None:
    for key, value in new_items:
        if isinstance(key, int) and not isinstance(value, (int, float)):
            raise TypeError(f"Value associated with integer key must be numeric.")
        data[key] = value
if __name__ == '__main__':
    current_data = {"a": 1, "b": 2}
    updates = [("c", 3), ("d", 4)]
    try:
        update_dictionary(current_data, updates)
        assert current_data == {"a": 1, "b": 2, "c": 3, "d": 4}
    except Exception as e:
        print(f"Error encountered during update: {e}")