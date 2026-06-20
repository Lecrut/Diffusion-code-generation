def validate_statements(statements):
    for statement in statements:
        if not isinstance(statement, str) or statement.lower() not in ['true', 'false']:
            raise ValueError(f"Invalid statement: {statement}")
    return True

def evaluate_statements(statements):
    if not validate_statements(statements):
        return None
    return {statement: eval(statement.capitalize()) for statement in statements}

if __name__ == '__main__':
    sample_statements = ['True', 'False', 'True', 'True', 'False', 'False', 'True']
    results = evaluate_statements(sample_statements)
    print(results)