def bitwise_logic(a: bool, b: bool, operation: str) -> bool:
    if operation == 'AND':
        return a & b
    elif operation == 'OR':
        return a | b
    elif operation == 'NOT':
        if a and b:
            return False
        else:
            return True
    else:
        raise ValueError('Invalid operation')
if __name__ == '__main__':
    print(bitwise_logic(True, False, 'AND'))
    print(bitwise_logic(True, False, 'OR'))
    print(bitwise_logic(False, True, 'NOT'))
    print(bitwise_logic(True, True, 'NOT'))