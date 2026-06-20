def evaluate_tf_statements(statements):
    return {statement: eval(statement) for statement in statements}

if __name__ == '__main__':
    sample_values = ['True', 'False', '2 + 2 == 4', '3 > 5']
    print(evaluate_tf_statements(sample_values))