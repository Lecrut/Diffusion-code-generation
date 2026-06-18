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
    print("Original data:", sample_data)
    try:
        removed_by_key = remove_by_key(sample_data, "banana")
        if removed_by_key:
            print(f"Removed by key 'banana'. Remaining keys: {list(sample_data.keys())}")
        remaining_values = list(sample_data.values())
        target_value_list = [5]
        try:
            result = remove_by_value(dict(zip(*zip(remaining_values, sample_data))), *target_value_list)
            print(f"Removed by value(s). Remaining data: {sample_data}")
        except Exception as e:
            print(f"Error during removal: {e}")
    except TypeError as te:
        print(f"Input validation error: {te}")