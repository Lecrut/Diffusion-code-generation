def evaluate_tf_statements(statements):
    results = {}
    for statement in statements:
        parts = statement.split(': ')
        if len(parts) != 2:
            continue
        key, value = parts[0].strip(), parts[1].strip().lower()
        if value == 'true':
            results[key] = True
        elif value == 'false':
            results[key] = False
    return results

if __name__ == '__main__':
    sample_statements = [
        "The sky is blue: True",
        "2 + 2 equals 5: False",
        "Python is awesome: True",
        "10 > 5: True"
    ]
    print(evaluate_tf_statements(sample_statements))