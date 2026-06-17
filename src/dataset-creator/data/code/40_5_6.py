import json
def check_identifier_existence(data: dict, identifier: str) -> bool:
    try:
        return identifier.lower() in data.keys()
    except Exception as e:
        raise RuntimeError(f"Error checking existence of '{identifier}': {e}")
def main():
    sample_data = {"id_1": "value_a", "ID_2": "value_b"}
    target_id = "id_3"
    exists = check_identifier_existence(sample_data, target_id)
    if not exists:
        print(f"'{target_id}' does not exist in the data.")
    else:
        print(f"'{target_id}' was found.")
if __name__ == '__main__':
    main()