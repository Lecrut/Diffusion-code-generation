OPERATIONS = {
    'AND': lambda a, b: a and b,
    'OR': lambda a, b: a or b,
}

def parse_logical_statement(statement, A, B):
    parts = statement.split()
    if len(parts) != 3:
        raise ValueError("Invalid statement format")
    operator = parts[1]
    return OPERATIONS.get(operator)(A, B)

if __name__ == '__main__':
    print(parse_logical_statement('A AND B', True, False))
    print(parse_logical_statement('B OR A', False, True))