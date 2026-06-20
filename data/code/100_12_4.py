def parse_logical_statement(statement, A, B):
    if statement == 'A AND B':
        return A and B
    elif statement == 'A OR B':
        return A or B
    elif statement == 'NOT A':
        return not A
    else:
        raise ValueError('Unsupported logical statement')
if __name__ == '__main__':
    result = parse_logical_statement('A AND B', True, False)
    print(result)