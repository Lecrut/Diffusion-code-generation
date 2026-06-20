TRUE_VALUES = {'true', 't', '1', 'yes'}
FALSE_VALUES = {'false', 'f', '0', 'no'}

def evaluate_tf_statements(statements):
    results = {}
    for statement in statements:
        parts = statement.split(': ')
        if len(parts) != 2:
            continue
        key, value = parts[0].strip(), parts[1].lower().strip()
        results[key] = value in TRUE_VALUES
    return results

if __name__ == '__main__':
    sample_statements = [
        "The sky is blue: True",
        "2 + 2 equals 5: False",
        "Python is awesome: True",
        "10 > 5: True"
    ]
    print(evaluate_tf_statements(sample_statements))