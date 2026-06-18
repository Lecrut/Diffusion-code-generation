def remove_by_key(dictionary: dict, key) -> None:
    if not isinstance(dictionary, dict):
        raise TypeError("The first argument must be a dictionary.")
    if key is None:
        raise ValueError("Key cannot be None.")
    try:
        del dictionary[key]
    except KeyError as e:
        print(f"Error: Key '{key}' not found in the dictionary. ({e})")
def remove_by_value(dictionary: dict, value) -> int:
    if not isinstance(dictionary, dict):
        raise TypeError("The first argument must be a dictionary.")
    count = 0
    keys_to_remove = [k for k in dictionary.keys() if dictionary[k] == value]
    for key in reversed(keys_to_remove):
        del dictionary[key]
        count += 1
    return count
if __name__ == '__main__':
    sample_data = {
        "apple": 5,
        "banana": 3,
        "cherry": 2,
        "date": 4,
        "elderberry": 6
    }
    remove_by_key(sample_data, "banana")
    print(f"Dictionary after removing 'banana': {sample_data}")
    sample_data = {
        "apple": 5,
        "banana": 3,
        "cherry": 2,
        "date": 4,
        "elderberry": 6
    }
    removed_count = remove_by_value(sample_data, 3)
    print(f"Removed {removed_count} entries with value 3.")
    print(f"Dictionary after removing values equal to 3: {sample_data}")
    try:
        remove_by_key({"a": 1}, "nonexistent")
    except ValueError as e:
        pass
    try:
        remove_by_value("not a dict", 3)
    except TypeError as e:
        print(f"Caught expected type error during value removal.")