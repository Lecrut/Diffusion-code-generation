def validate_and_evaluate(statement):
    if not isinstance(statement, str):
        raise ValueError("Input must be a string")
    
    statement = statement.strip().lower()
    if statement not in {'true', 'false'}:
        raise ValueError(f"Invalid value encountered: '{statement}'")
    
    return statement == 'true'

if __name__ == '__main__':
    sample_values = ['true', ' false ', 'TRUE', 'FALSE']
    results = [validate_and_evaluate(value) for value in sample_values]
    print(results)