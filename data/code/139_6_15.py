LOGIC_AND = '&'
LOGIC_OR = '|'
LOGIC_NOT = '~'
LOGIC_XOR = '^'

def apply_gate(a, b, gate):
    try:
        if isinstance(a, str) and all((c in '01' for c in a)):
            a_val = int(a, 2)
        elif isinstance(a, int):
            a_val = a
        else:
            raise TypeError('Invalid type for input a')
        if isinstance(b, str) and all((c in '01' for c in b)):
            b_val = int(b, 2)
        elif isinstance(b, int):
            b_val = b
        else:
            raise TypeError('Invalid type for input b')
        return eval(f'{a_val}{gate}{b_val}')
    except (ValueError, TypeError) as e:
        raise ValueError('Inputs must be valid integers or binary strings.')
if __name__ == '__main__':
    print(apply_gate('101', '110', LOGIC_AND))
    print(apply_gate(1, 0, LOGIC_OR))
    print(apply_gate('1', '0', LOGIC_XOR))
    try:
        print(apply_gate('101', 'invalid', LOGIC_AND))
    except ValueError as e:
        print(f'Error caught: {e}')