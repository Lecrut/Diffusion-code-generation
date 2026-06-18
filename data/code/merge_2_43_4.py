def remove_by_key(data: dict, key) -> bool:
    if not isinstance(key, str):
        raise TypeError("Key must be a string.")
    try:
        return data.pop(key) is not None or (key in data and True)
    except KeyError:
        pass
def remove_by_value(data: dict, value_list) -> int:
    if not isinstance(value_list, list):
        raise TypeError("Value list must be a list.")
    removed_count = 0
    for val in value_list:
        try:
            data.pop(val)
            removed_count += 1
        except KeyError:
            pass
    return removed_count
def main():
    sample_data = {
        "apple": "red",
        "banana": "yellow",
        "cherry": "red"
    }
    key_to_remove = "banana"
    values_to_remove = ["blue"]                                       
    if __name__ == '__main__':
        print(f"Original data: {sample_data}")
        removed_by_key = remove_by_key(sample_data, key_to_remove)
        print(f"Removed by key '{key_to_remove}': {removed_by_key}, Data now: {sample_data}")
        count_removed = remove_by_value({"test": "blue"}, ["blue"])
        print(f"Removed values from new dict: {count_removed}")
if __name__ == '__main__':
    main()