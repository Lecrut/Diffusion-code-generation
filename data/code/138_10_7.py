def and_operation(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a and b

def or_operation(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a or b

def not_operation(a):
    if not isinstance(a, bool):
        raise ValueError("Input must be a boolean value.")
    return not a

def nand_operation(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return not (a and b)

def nor_operation(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return not (a or b)

def xor_operation(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a != b

def xnor_operation(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a == b

if __name__ == '__main__':
    print("A | B | A AND B")
    print("---|---|---------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A} | {B} | {and_operation(A, B)}")

    print("\nA | B | A OR B")
    print("---|---|--------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A} | {B} | {or_operation(A, B)}")

    print("\nA | NOT A")
    print("---|------")
    for A in [True, False]:
        print(f"{A} | {not_operation(A)}")

    print("\nA | B | A NAND B")
    print("---|---|---------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A} | {B} | {nand_operation(A, B)}")

    print("\nA | B | A NOR B")
    print("---|---|--------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A} | {B} | {nor_operation(A, B)}")

    print("\nA | B | A XOR B")
    print("---|---|---------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A} | {B} | {xor_operation(A, B)}")

    print("\nA | B | A XNOR B")
    print("---|---|---------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A} | {B} | {xnor_operation(A, B)}")