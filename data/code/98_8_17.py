def filter_records(records):
    if not isinstance(records, (list, tuple)):
        raise ValueError("Input must be a list or tuple of records")
    
    result = []
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Each record must be a dictionary")
        
        value = record.get('value')
        category = record.get('category')
        
        if value is None or category is None:
            raise ValueError("Record must contain 'value' and 'category' keys")
        
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be numeric")
        
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
            
        condition_a = (value > 100) and (category == 'A')
        condition_b = (value == 0)
        
        if condition_a or condition_b:
            result.append(record)
            
    return result

if __name__ == '__main__':
    sample_data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 101, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 101, 'category': 'A'}
    ]
    
    print(filter_records(sample_data))