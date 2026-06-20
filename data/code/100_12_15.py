def parse_logical_statement(statement, a, b):
    if statement == 'A AND B':
        return a and b
    elif statement == 'A OR B':
        return a or b
    else:
        raise ValueError('Unsupported logical operation')
if __name__ == '__main__':
    result = parse_logical_statement('A AND B', True, False)
    print(result)