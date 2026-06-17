import json
def append_entry(data_structure: list, entry_type: str) -> None:
    valid_types = ['string', 'integer', 'float']
    if not isinstance(entry_type, str):
        raise TypeError("Entry type must be a string.")
    if entry_type.lower() == "string":
        try:
            new_entry = input("Enter string value:")
            data_structure.append({"type": "string", "value": new_entry})
        except ValueError as e:
            print(f"Error processing string input: {e}")
    elif entry_type.lower() in ["integer", "float"]:
        try:
            raw_input = input("Enter numeric value:")
            if entry_type.lower() == "integer":
                new_entry = int(raw_input)
            else:
                new_entry = float(raw_input)
            data_structure.append({"type": entry_type, "value": new_entry})
        except ValueError as e:
            print(f"Error processing numeric input: {e}")
if __name__ == '__main__':
    sample_data = []
    test_inputs = [
        ("string", "Hello, World!"),
        ("integer", 42),
        ("float", 3.14)
    ]
    print("Starting data append process...")
    for entry_type, value in test_inputs:
        try:
            if isinstance(value, str):
                sample_data.append({"type": "string", "value": value})
            elif isinstance(value, int):
                sample_data.append({"type": "integer", "value": value})
            else:
                sample_data.append({"type": float(entry_type), "value": value if not isinstance(value, str) and '.' in str(value) or entry_type == 'float' else 0.0})                                
        except Exception as e:
            print(f"Error during append simulation: {e}")
    sample_data.append({"type": "string", "value": "Final Test Entry"})
    output = json.dumps(sample_data, indent=4)
    print("Appended data structure:")
    print(output)