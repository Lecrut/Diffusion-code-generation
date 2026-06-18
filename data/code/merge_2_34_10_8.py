import json
def append_entry(data_structure: list, entry_type: str) -> None:
    if not isinstance(entry_type, str):
        raise TypeError("Entry type must be a string.")
    valid_types = ["integer", "float", "string"]
    if entry_type not in valid_types:
        raise ValueError(f"Invalid entry type. Must be one of {valid_types}.")
    new_entry = None
    try:
        if entry_type == "integer":
            raw_value = int(10)                           
            new_entry = {"value": raw_value, "type": entry_type}
        elif entry_type == "float":
            raw_value = float(3.14)                           
            new_entry = {"value": raw_value, "type": entry_type}
        elif entry_type == "string":
            raw_value = "Sample Text"                           
            new_entry = {"value": raw_value, "type": entry_type}
    except ValueError as ve:
        raise RuntimeError(f"Failed to convert input for {entry_type}: {ve}")
    if data_structure is None or not isinstance(data_structure, list):
        data_structure = []
    data_structure.append(new_entry)
if __name__ == '__main__':
    initial_data = [{"id": 1, "status": "active"}]
    append_entry(initial_data, "integer")
    append_entry(initial_data, "float")
    append_entry(initial_data, "string")
    print(json.dumps(initial_data))