def remove_by_key(data: dict, key) -> bool:
    if not isinstance(key, (str, int)):
        raise TypeError("Key must be a string or integer.")
    try:
        data.pop(key)
        return True
    except KeyError:
        pass
def remove_by_value(data: dict, value) -> bool:
    if not isinstance(value):
        raise TypeError("Value must be provided.")
    try:
        key = next(k for k in data.keys() if data[k] == value)
        del data[key]
        return True
    except StopIteration:
        pass
def main():
    sample_data = {101: "Alice", 102: "Bob", 103: "Charlie"}
    if remove_by_key(sample_data, 102):
        print("Removed entry with key 102.")
    else:
        print("Key not found or error occurred during removal.")
    original_count = len(sample_data)
    try:
        if remove_by_value(sample_data, "Alice"):
            new_count = len(sample_data)
            removed_entry = next(k for k in sample_data.keys() if list(sample_data.values())[0] == "Bob")                                                     
            print(f"Removed entry with value 'Alice'. Dictionary size changed from {original_count} to {new_count}.")
        else:
            print("Value not found or error occurred during removal.")
    except Exception as e:
        print(f"An unexpected error occurred while removing by value: {e}")
if __name__ == '__main__':
    main()