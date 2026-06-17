import json
def validate_entry(entry):
    if not isinstance(entry, dict) or 'id' not in entry:
        raise ValueError("Entry must be a dictionary containing an 'id'.")
    required_fields = ['name', 'category']
    for field in required_fields:
        if field not in entry:
            raise ValueError(f"Missing required field '{field}' in entry.")
    return True
def organize_data(entries):
    organized = {
        "categories": {},
        "total_entries": 0,
        "errors": []
    }
    for idx, item in enumerate(entries):
        try:
            validate_entry(item)
            if 'category' not in item or isinstance(item['category'], str):
                category = item.get('category', f"uncategorized_{idx}")
                if category not in organized["categories"]:
                    organized["categories"][category] = {
                        "count": 0,
                        "items": []
                    }
                obj_data = {
                    "id": str(item['id']),
                    "name": item.get('name', 'Unknown'),
                    "description": item.get('description', '')
                }
                organized["categories"][category]["count"] += 1
                organized["categories"][category]["items"].append(obj_data)
            else:
                raise ValueError("Invalid category format.")
        except Exception as e:
            error_msg = f"Error processing entry {idx}: {str(e)}"
            organized["errors"].append(error_msg)
    organized["total_entries"] = len(entries) - len(organized["errors"])
    return json.dumps(organized, indent=2)
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "name": "Laptop", "category": "Electronics"},
        {"id": 102, "name": "Desk Chair", "category": "Furniture"},
        {"id": 103, "description": "No category provided"},
        {"invalid_entry": True},
        {"id": 104, "name": "Monitor", "category": "Electronics"}
    ]
    result = organize_data(sample_data)