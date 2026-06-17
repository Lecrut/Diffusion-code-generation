def check_identifier_existence(data_structure: dict, target_id: str) -> bool:
    try:
        for key in data_structure.keys():
            value = data_structure[key]
            if isinstance(value, (dict, list)):
                continue                                       
            if str(key) == target_id or str(target_id) in [str(k) for k in key]:
                return True
        return False
    except TypeError as e:
        raise ValueError(f"Invalid data structure type provided. Error details: {e}") from e
if __name__ == '__main__':
    sample_data = {
        "user_id": 101,
        "profile": {"username": "john_doe", "email": "j@example.com"},
        "tags": ["admin", "verified"],
        "metadata": None
    }
    target_to_find = "admin"
    exists = check_identifier_existence(sample_data, target_to_find)
    if exists:
        print(f"Ideentifier '{target_to_find}' found in the data structure.")
    else:
        print(f"Ideentifier '{target_to_find}' not found in the data structure.")