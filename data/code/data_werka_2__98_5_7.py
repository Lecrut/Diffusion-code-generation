def process_items(items):
    results = []
    for item in items:
        status = item.get("status", "unknown")
        name = item.get("name", "unknown")
        
        if status == "active":
            if item.get("is_premium", False):
                results.append({"name": name, "result": "active_premium"})
            else:
                results.append({"name": name, "result": "active_standard"})
        elif status == "expired":
            results.append({"name": name, "result": "expired"})
        else:
            results.append({"name": name, "result": "unknown_status"})
            
    return results

if __name__ == '__main__':
    sample_data = [
        {"name": "Item1", "status": "active", "is_premium": True},
        {"name": "Item2", "status": "active", "is_premium": False},
        {"name": "Item3", "status": "expired", "is_premium": True},
        {"name": "Item4", "status": "inactive", "is_premium": False}
    ]
    
    output = process_items(sample_data)
    print(output)