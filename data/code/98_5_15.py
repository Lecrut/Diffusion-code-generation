def process_items(items):
    processed_results = []
    for item in items:
        result = {"id": item.get("id"), "status": "default"}
        if item.get("active", False):
            result["status"] = "Active"
        elif item.get("premium", False):
            result["status"] = "Premium"
        elif item.get("expiry_date") and item.get("expiry_date") < '2023-01-01':
            result["status"] = "Expired"
        processed_results.append(result)
    return processed_results

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Item A", "active": True, "premium": False, "expiry_date": None},
        {"id": 2, "name": "Item B", "active": False, "premium": True, "expiry_date": '2022-12-31'},
    ]
    print(process_items(sample_data))