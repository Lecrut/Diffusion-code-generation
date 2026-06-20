def evaluate_statement(statement):
    return statement == 'true'

if __name__ == '__main__':
    sample_statements = [
        "true",
        "false",
        "1 == 1",
        "2 + 2 == 5"
    ]
    
    results = {statement: evaluate_statement(statement) for statement in sample_statements}
    print(results)