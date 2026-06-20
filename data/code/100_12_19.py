OPERATORS = {
    'AND': lambda x, y: x and y,
    'OR': lambda x, y: x or y
}

def parse_statement(statement):
    parts = statement.split()
    if len(parts) != 3:
        raise ValueError("Invalid input format")
    operand1 = parts[0]
    operator = parts[1]
    operand2 = parts[2]
    return OPERATORS.get(operator, lambda x, y: False)(operand1 == 'True', operand2 == 'True')

if __name__ == '__main__':
    statement1 = 'A AND B'
    statement2 = 'A OR B'
    print(f"Statement 1: {statement1}, Result: {parse_statement(statement1)}")
    print(f"Statement 2: {statement2}, Result: {parse_statement(statement2)}")