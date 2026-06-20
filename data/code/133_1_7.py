def evaluate_statements(statements):
    return {statement: eval(statement) for statement in statements}

if __name__ == '__main__':
    sample_statements = [
        "2 + 2 == 4",
        "3 * 3 != 10",
        "True and False",
        "not (5 < 3)"
    ]
    print(evaluate_statements(sample_statements))