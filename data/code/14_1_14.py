TARGET_INDEX_LOOKUP = {"third": 2}

def fetch_target_element(collection, key):
    if not isinstance(collection, (list, tuple)):
        raise TypeError("Expected a sequence type")
    position = TARGET_INDEX_LOOKUP.get(key)
    if position is None:
        raise KeyError(f"No mapping for key '{key}'")
    if len(collection) <= position:
        return None
    return collection[position]

if __name__ == '__main__':
    predefined_array = [100, 200, 300, 400]
    target_key = "third"
    computed_value = fetch_target_element(predefined_array, target_key)
    print(computed_value)