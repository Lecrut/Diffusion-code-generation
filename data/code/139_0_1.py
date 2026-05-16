def and_gate(a, b):
    return a and b
def or_gate(a, b):
    return a or b
def not_gate(a):
    return not a
if __name__ == '__main__':
    A = True
    B = False
    print("--- AND Gate ---")
    result_and = and_gate(A, B)
    print(f"A: {A}, B: {B}")
    print(f"A AND B: {result_and}")
    print("\n--- OR Gate ---")
    result_or = or_gate(A, B)
    print(f"A: {A}, B: {B}")
    print(f"A OR B: {result_or}")
    print("\n--- NOT Gate ---")
    result_not = not_gate(A)
    print(f"A: {A}")
    print(f"NOT A: {result_not}")