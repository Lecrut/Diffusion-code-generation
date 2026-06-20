def evaluate_statements(statements):
    return {statement: eval(statement) for statement in statements}

if __name__ == '__main__':
    sample_statements = ['True', 'False', '2 + 2 == 4', '3 > 5']
    results = evaluate_statements(sample_statements)
    print(results)