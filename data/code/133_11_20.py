def evaluate_statement(statement):
    return eval(statement)

if __name__ == '__main__':
    statements = ['True', 'False', '2 + 2 == 4', '3 > 5']
    results = [evaluate_statement(stmt) for stmt in statements]
    print(results)