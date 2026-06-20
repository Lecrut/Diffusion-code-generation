def and_op(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise TypeError('Inputs must be boolean values')
    return a and b

def or_op(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise TypeError('Inputs must be boolean values')
    return a or b

def not_op(a):
    if not isinstance(a, bool):
        raise TypeError('Input must be a boolean value')
    return not a

if __name__ == '__main__':
    val_a = True
    val_b = False
    print(f"Value A: {val_a}")
    print(f"Value B: {val_b}")
    print("AND Operation Result:", and_op(val_a, val_b))
    print("OR Operation Result:", or_op(val_a, val_b))
    print("NOT Operation Result:", not_op(val_a))