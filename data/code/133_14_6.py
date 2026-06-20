def evaluate_tf_statements(statements):
    return {s: eval(s) for s in statements}

if __name__ == '__main__':
    sample_values = ['True', 'False', '2 > 1', '3 < 2']
    print(evaluate_tf_statements(sample_values))