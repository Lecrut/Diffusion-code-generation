def process_items(items):
    processed_results = []
    for item in items:
        result = {"id": item.get("id"), "status": "default"}
        if item.get("active"):
            result["status"] = "Active"
        elif item.get("premium"):
            result["status"] = "Premium"
        elif item.get("expired"):
            result["status"] = "Expired"
        else:
            result["status"] = "Inactive"
        processed_results.append(result)
    return processed_results
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Item A", "active": True, "premium": False, "expired": False},
        {"id": 2, "name": "Item B", "active": False, "premium": True, "expired": False},
        {"id": 3, "name": "Item C", "active": False, "premium": False, "expired": True},
        {"id": 4, "name": "Item D", "active": True, "premium": True, "expired": False},
        {"id": 5, "name": "Item E", "active": False, "premium": False, "expired": False}
    ]
    output = process_items(sample_data)
    for item in output:
        print(item)