def evaluate_statements(statements):
    true_count = 0
    false_count = 0
    for statement in statements:
        if statement == 'True':
            true_count += 1
        elif statement == 'False':
            false_count += 1
    return (true_count, false_count)
if __name__ == '__main__':
    sample_statements = ['True', 'False', 'True', 'True', 'False', 'False', 'True']
    result = evaluate_statements(sample_statements)
    print(result)