import json
def append_entry(data_structure: list, entry_type: str) -> None:
    if not isinstance(entry_type, str):
        raise TypeError("Entry type must be a string.")
    valid_types = ['integer', 'float', 'string']
    if entry_type not in valid_types:
        raise ValueError(f"Unsupported entry type. Expected one of {valid_types}.")
    new_entry = {}
    new_entry['type'] = entry_type
    try:
        if entry_type == 'integer':
            value = int(10)                             
            new_entry['value'] = value
        elif entry_type == 'float':
            value = float(3.14)                           
            new_entry['value'] = value
        elif entry_type == 'string':
            value = "Sample Text"                            
            new_entry['value'] = value
    except ValueError as ve:
        raise RuntimeError(f"Failed to parse value for type {entry_type}: {ve}") from ve
    data_structure.append(new_entry)
if __name__ == '__main__':
    existing_data = []
    append_entry(existing_data, 'integer')
    append_entry(existing_data, 'float')
    append_entry(existing_data, 'string')
    print(json.dumps(existing_data))