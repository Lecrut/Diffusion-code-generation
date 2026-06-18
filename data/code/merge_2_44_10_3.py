def get_nested_value(data: dict, *keys) -> any:
    current = data
    if not isinstance(current, dict):
        raise TypeError("Expected input to be a dictionary.")
    try:
        for key in keys:
            if not isinstance(key, str) or key == "":
                return None                                         
            current = current.get(key)
            if current is None:
                break
    except Exception as e:
        print(f"An error occurred during navigation: {e}")
    return current
def main():
    database = {
        "company": {
            "name": "Acme Corp",
            "departments": [
                {"id": 1, "name": "Engineering"},
                {"id": 2, "name": "Sales"}
            ]
        },
        "products": ["Widget A", "Gadget B"],
        "metadata": {
            "version": "1.0",
            "status": "active"
        }
    }
    result_1 = get_nested_value(database, "company", "name")
    result_2 = get_nested_value(database, "nonexistent_key", "value")
    result_3 = get_nested_value(database, "metadata", "status")
    print(f"Company Name: {result_1}")
    if result_2 is None:
        print("Path not found (Expected)")
    print(f"Status: {result_3}")
if __name__ == '__main__':
    main()