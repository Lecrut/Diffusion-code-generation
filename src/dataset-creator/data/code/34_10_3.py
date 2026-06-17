import json
def append_entry(data_structure: list, entry_type: str, new_value) -> None:
    if not isinstance(entry_type, str):
        raise TypeError("Entry type must be a string.")
    valid_types = ["int", "float", "str"]
    if entry_type.lower() not in valid_types:
        return
    try:
        parsed_value = eval(f"{'f' * (entry_type == 'float')}{new_value}")
        if isinstance(parsed_value, int) and entry_type != "int":
            raise ValueError("Value mismatch for type specification.")
        data_structure.append({"type": entry_type.lower(), "value": parsed_value})
    except Exception as e:
        print(f"Error processing value {new_value}: {e}")
if __name__ == '__main__':
    database = []
    append_entry(database, "int", 42)
    append_entry(database, "float", 3.14)
    append_entry(database, "str", "hello")
    print(json.dumps(database))