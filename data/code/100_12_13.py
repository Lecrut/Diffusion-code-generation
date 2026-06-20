def evaluate_statement(statement, var_a, var_b):
    if statement == 'A AND B':
        return var_a and var_b
    elif statement == 'A OR B':
        return var_a or var_b
    elif statement == 'NOT A':
        return not var_a
    elif statement == 'NOT B':
        return not var_b
    else:
        raise ValueError("Unsupported logical operation")

if __name__ == '__main__':
    result1 = evaluate_statement('A AND B', True, False)
    print(f"Result 1: {result1}")