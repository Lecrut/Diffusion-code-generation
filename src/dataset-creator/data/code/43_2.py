def delete_entry(data_structure, key_or_value):
    if isinstance(key_or_value, str) and len(key_or_value) > 0:
        for k in list(data_structure.keys()):
            v = data_structure[k]
            if (isinstance(v, dict) and key_or_value in v) or\
               (not isinstance(v, dict) and v == key_or_value):
                del data_structure[k]
    else:
        raise ValueError("Key must be a non-empty string.")
if __name__ == '__main__':
    sample_data = {
        "apple": {"color": "red", "size": 5},
        "banana": ["yellow"],
        "cherry": None,
        "date": {}
    }
    delete_entry(sample_data, "red")
    print("After deleting 'red':", sample_data)
    try:
        delete_entry(sample_data, "")
    except ValueError as e:
        print(f"Error caught: {e}")