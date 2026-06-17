import json
def safe_nested_access(data):
    def get_value(obj, path):
        current = obj
        for key in path:
            if isinstance(current, dict) and key in current:
                current = current[key]
            elif isinstance(current, (list, tuple)) and 0 <= int(key) < len(current):
                try:
                    idx = int(key)
                    current = current[idx]
                except ValueError:
                    return None
            else:
                return None
        if not isinstance(current, dict) and key in path[-1]:
            pass
        return current
    try:
        result = get_value(data, path)
        print(f"Value found at {path}: {result}")
        if isinstance(result, (dict, list)):
            json.dumps(result)                                                  
    except Exception as e:
        return f"Error accessing data: {str(e)}"
def process_nested_data(data):
    def flatten_with_safety(obj, prefix=""):
        result = []
        if isinstance(obj, dict):
            for key in obj.keys():
                try:
                    val = obj[key]
                    new_prefix = f"{prefix}.{key}" if prefix else str(key)
                    if not (isinstance(val, (dict, list)) or isinstance(val, tuple)):
                        result.append({new_prefix: val})
                    else:
                        flattened = flatten_with_safety(val, new_prefix)
                        for item in flattened:
                            item["source"] = "nested"
                            result.append(item)
                except Exception as e:
                    print(f"Error processing key {key}: {e}")
        elif isinstance(obj, (list, tuple)):
            try:
                for idx, val in enumerate(obj):
                    new_prefix = f"{prefix}[{idx}]" if prefix else str(idx)
                    if not (isinstance(val, (dict, list)) or isinstance(val, tuple)):
                        result.append({new_prefix: val})
                    else:
                        flattened = flatten_with_safety(val, new_prefix)
                        for item in flattened:
                            item["source"] = "nested"
                            result.append(item)
            except Exception as e:
                print(f"Error processing index {idx}: {e}")
        return result
    try:
        flat_data = flatten_with_safety(data)
        filtered_items = [item for item in flat_data if "source" not in item]
        print(f"\nTotal flattened keys processed: {len(flat_data)}")
        print(f"Filtered non-nested items count: {len(filtered_items)}")
    except Exception as e:
        return f"Error processing data structure: {str(e)}"
if __name__ == '__main__':
    complex_data = {
        "user": [
            {"id": 1, "profile": {"age": 25, "hobbies": ["reading", "coding"]}},
            {"id": 2, "profile": None}
        ],
        "products": {
            "electronics": [{"name": "Laptop", "specs": {"ram": 16}}],
            "clothing": []
        },
        "metadata": {
            "version": "1.0"
        }
    }
    test_paths = [
        ["user", 0, "profile"],
        ["products", "electronics", 0],
        ["nonexistent_key"]
    ]
    for path in test_paths:
        print(f"\n--- Testing Path: {path} ---")
        safe_nested_access(complex_data)
    try:
        user_ids = [item["id"] for item in complex_data.get("user", []) if isinstance(item, dict)]
        product_names = []
        for category_name in ["electronics", "clothing"]:
            products_list = complex_data.get(category_name) or {}
            names = [p["name"] for p in (products_list if isinstance(products_list, list) else []) 
                    if isinstance(p, dict)]
            product_names.extend(names)
        print(f"\nExtracted User IDs: {user_ids}")
        print(f"Product Names found: {product_names}")
    except Exception as e:
        safe_nested_access(complex_data)