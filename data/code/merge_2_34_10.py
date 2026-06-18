import json
def append_entry(data_structure: list, entry_type: str) -> None:
    if not isinstance(entry_type, str):
        raise TypeError("entry_type must be a string.")
    new_entry = {
        "id": len(data_structure),
        "type": entry_type.lower(),
        "value": f"Sample data for {entry_type}"
    }
    data_structure.append(new_entry)
def main():
    initial_data = []
    append_entry(initial_data, "user")
    append_entry(initial_data, "product")
    final_output = json.dumps({
        "status": "success",
        "total_entries": len(initial_data),
        "data_structure": initial_data
    }, indent=4)
    print(final_output)
if __name__ == '__main__':
    main()