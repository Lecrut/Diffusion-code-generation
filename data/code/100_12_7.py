def evaluate_statement(statement, A, B):
    if statement == 'A AND B':
        return A and B
    elif statement == 'A OR B':
        return A or B
    elif statement == 'NOT A':
        return not A
    else:
        raise ValueError("Unsupported statement")

if __name__ == '__main__':
    print(evaluate_statement('A AND B', True, False))
    print(evaluate_statement('A OR B', True, False))
    print(evaluate_statement('NOT A', False))