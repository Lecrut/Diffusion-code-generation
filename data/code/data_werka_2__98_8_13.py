def filter_records(data):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Input must be a list or tuple of records.")

    result = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each record must be a dictionary.")
        value = item.get("value")
        category = item.get("category")
        
        if value is None or category is None:
            raise ValueError("Records must contain 'value' and 'category' keys.")
        
        value_valid = isinstance(value, (int, float))
        category_valid = isinstance(category, str)
        
        if not value_valid or not category_valid:
            raise ValueError("Value must be numeric and category must be a string.")

        condition_1 = (value > 100) and (category == "A")
        condition_2 = (value == 0)
        
        if condition_1 or condition_2:
            result.append(item)
            
    return result

if __name__ == '__main__':
    raw_data = [
        {"value": 150, "category": "A"},
        {"value": 50, "category": "A"},
        {"value": 200, "category": "B"},
        {"value": 0, "category": "A"},
        {"value": 100, "category": "A"},
        {"value": 101, "category": "B"},
        {"value": 0, "category": "B"},
        {"value": -10, "category": "A"},
        {"value": 100.0001, "category": "A"}
    ]
    
    output = filter_records(raw_data)
    print(output)