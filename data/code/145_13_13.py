def validate_data(data):
    results = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each element must be a dictionary")
        
        required_fields = {'name', 'age', 'email'}
        missing_fields = required_fields - set(item.keys())
        if missing_fields:
            raise ValueError(f"Missing fields: {missing_fields}")
        
        if not isinstance(item['age'], int) or item['age'] < 0:
            raise ValueError("Age must be a non-negative integer")
        
        if not isinstance(item['email'], str) or '@' not in item['email']:
            raise ValueError("Email must be a valid string")
        
        results.append(True)
    return results

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
        {'name': 'Bob', 'age': -5, 'email': 'bob@.com'}
    ]
    
    try:
        results = validate_data(sample_data)
        print(results)
    except ValueError as e:
        print(e)