def bitwise_logic(a: bool, b: bool, operation: str) -> bool:
    if operation == 'AND':
        return a & b
    elif operation == 'OR':
        return a | b
    elif operation == 'NOT':
        return not a
    else:
        raise ValueError('Invalid operation')
if __name__ == '__main__':
    print(bitwise_logic(True, False, 'AND'))
    print(bitwise_logic(True, True, 'OR'))
    print(bitwise_logic(False, False, 'NOT'))