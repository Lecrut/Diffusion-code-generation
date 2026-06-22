def process_items(items):
    results = []
    for item in items:
        name = item.get("name", "")
        status = item.get("status", "")
        is_premium = item.get("is_premium", False)
        
        if status == "active" and is_premium:
            results.append({"name": name, "category": "premium_active"})
        elif status == "active":
            results.append({"name": name, "category": "standard_active"})
        elif status == "expired" and is_premium:
            results.append({"name": name, "category": "premium_expired"})
        elif status == "expired":
            results.append({"name": name, "category": "standard_expired"})
        else:
            results.append({"name": name, "category": "unknown"})
    return results

if __name__ == '__main__':
    sample_data = [
        {"name": "User1", "status": "active", "is_premium": True},
        {"name": "User2", "status": "active", "is_premium": False},
        {"name": "User3", "status": "expired", "is_premium": True},
        {"name": "User4", "status": "expired", "is_premium": False},
        {"name": "User5", "status": "inactive", "is_premium": False}
    ]
    output = process_items(sample_data)
    print(output)