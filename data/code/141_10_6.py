def bitwise_logic(a: bool, b: bool, op: str) -> bool:
    if op == 'AND':
        return a & b
    elif op == 'OR':
        return a | b
    elif op == 'NOT':
        if a and b:
            return False
        else:
            return True
    else:
        raise ValueError('Invalid operation')
if __name__ == '__main__':
    print(bitwise_logic(True, False, 'AND'))
    print(bitwise_logic(True, True, 'OR'))
    print(bitwise_logic(False, False, 'NOT'))