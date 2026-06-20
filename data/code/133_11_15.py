def evaluate_statements(statements):
    truth_values = {'True': True, 'False': False}
    results = []
    for statement in statements:
        try:
            result = eval(statement, {}, truth_values)
            results.append(result)
        except Exception as e:
            results.append(f"Error: {e}")
    return results

if __name__ == '__main__':
    sample_statements = [
        "True",
        "False",
        "not True",
        "not False",
        "True and True",
        "True and False",
        "False and True",
        "False and False",
        "True or True",
        "True or False",
        "False or True",
        "False or False"
    ]
    
    results = evaluate_statements(sample_statements)
    print(results)