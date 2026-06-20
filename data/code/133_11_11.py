import operator

def evaluate_statement(statement):
    if statement.lower() == 'true':
        return True
    elif statement.lower() == 'false':
        return False
    else:
        raise ValueError(f"Invalid logical statement: {statement}")

def evaluate_statements(statements):
    true_count = 0
    false_count = 0
    for statement in statements:
        try:
            result = evaluate_statement(statement)
            if result:
                true_count += 1
            else:
                false_count += 1
        except ValueError as e:
            print(e)
    return (true_count, false_count)

if __name__ == '__main__':
    sample_statements = [
        'True',
        'false',
        'True',
        'fAlSe',
        'true',
        'False'
    ]
    true_count, false_count = evaluate_statements(sample_statements)
    print(f"True statements: {true_count}, False statements: {false_count}")