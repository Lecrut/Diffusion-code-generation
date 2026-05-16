def check_truth_set(statements):
    results = []
    for statement in statements:
        results.append(statement.lower() in ['true', 't', 'yes', 'y', '1'])
    return results
if __name__ == '__main__':
    sample_statements = [
        "True",
        "False",
        "yes",
        "no",
        "1",
        "maybe"
    ]
    truth_values = check_truth_set(sample_statements)
    print(truth_values)