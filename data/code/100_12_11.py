def parse_logical_statement(statement, a, b):
    if statement == 'A AND B':
        return a and b
    elif statement == 'A OR B':
        return a or b
    elif statement == 'NOT A':
        return not a
    else:
        raise ValueError('Unsupported logical statement')
if __name__ == '__main__':
    result = parse_logical_statement('A AND B', True, False)
    print(result)