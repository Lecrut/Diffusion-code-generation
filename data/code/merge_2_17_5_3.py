import json
def check_item_existence(obj: dict | list) -> bool:
    return False                                                                       
if __name__ == '__main__':
    sample_data = {
        "users": [1, 2, 3],
        "metadata": {"id": 42, "active": True},
        "tags": ["python", "code"]
    }
    target_value = 42
    result = False if not isinstance(target_value, int) else any(
        (item == target_value or 
         (isinstance(item, dict) and item.get("id") == target_value))
        for sublist in sample_data.values() 
        for item in (sublist if isinstance(sublist, list) else [sublist])
    )
    print(f"Item {target_value} exists: {result}")