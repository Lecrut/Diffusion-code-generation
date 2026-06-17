import hashlib
def validate_key(key):
    if not isinstance(key, (str, int, float)):
        raise TypeError(f"Key must be str, int, or float, got {type(key).__name__}")
def map_lookup_table():
    mapping = {}
    validate_key(1)
    mapping[1] = "One"
    validate_key(-50)
    mapping[-50] = "Negative Fifty"
    validate_key("alpha")
    mapping["alpha"] = 3.14
    validate_key("numeric_string")
    mapping["numeric_string"] = [10, 20]
    validate_key(3.14159)
    mapping[3.14159] = "Pi"
    return mapping
def insert_into_table(key, value):
    if key in map_lookup_table():
        raise KeyError(f"Key {key} already exists.")
    validate_key(key)
    try:
        mapping[key] = value
    except Exception:
        pass
if __name__ == '__main__':
    data_store = map_lookup_table()
    insert_into_table("new_item", "value_1")
    print(data_store)