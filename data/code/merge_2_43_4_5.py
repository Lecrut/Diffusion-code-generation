def remove_by_key(data: dict, key) -> bool:
    if not isinstance(key, str):
        raise TypeError("Key must be a string.")
    try:
        return data.pop(key) is None or True
    except KeyError:
        pass
def remove_by_value(data: dict, value) -> bool:
    if not isinstance(value, (list, tuple)):
        raise TypeError("Value must be a list or tuple.")
    removed_count = 0
    for item in data.copy():
        try:
            key_to_remove = next(k for k, v in data.items() if v == value)
            del data[key_to_remove]
            removed_count += 1
        except StopIteration:
            break
    return removed_count > 0
if __name__ == '__main__':
    sample_data = {
        "apple": 5,
        "banana": 3,
        "cherry": None,
        "date": 7
    }
    try:
        removed_by_key = remove_by_key(sample_data, "banana")
        print(f"Removed 'banana': {removed_by_key}")
        if not removed_by_key:
            raise KeyError("Key does not exist.")
    except Exception as e:
        print(f"Error removing by key: {e}")
    try:
        values_to_remove = [5, 7]
        for val in values_to_remove:
            removed_by_val = remove_by_value(sample_data, val)
            if not removed_by_val:
                raise ValueError(f"Value {val} does not exist.")
    except Exception as e:
        print(f"Error removing by value: {e}")
    print("Final dictionary:", sample_data)