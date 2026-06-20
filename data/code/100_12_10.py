def evaluate_logical_statement(statement, A, B):
    if statement == 'A AND B':
        return A and B
    elif statement == 'A OR B':
        return A or B
    elif statement == 'NOT A':
        return not A
    elif statement == 'NOT B':
        return not B
    else:
        raise ValueError("Unsupported logical statement")

if __name__ == '__main__':
    result1 = evaluate_logical_statement('A AND B', True, False)
    print(f"Result 1: {result1}")
    
    result2 = evaluate_logical_statement('A OR B', False, True)
    print(f"Result 2: {result2}")
    
    result3 = evaluate_logical_statement('NOT A', False)
    print(f"Result 3: {result3}")
    
    result4 = evaluate_logical_statement('NOT B', True)
    print(f"Result 4: {result4}")