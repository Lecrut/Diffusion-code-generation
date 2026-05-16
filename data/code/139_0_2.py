def and_gate(a, b):
    return a and b
def or_gate(a, b):
    return a or b
def not_gate(a):
    return not a
if __name__ == '__main__':
    A = True
    B = False
    not_A = not A
    result_and = and_gate(A, B)
    result_or = or_gate(A, B)
    result_not = not_gate(A)
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"NOT A: {result_not}")
    print(f"AND (A, B): {result_and}")
    print(f"OR (A, B): {result_or}")