def and_gate(a, b):
    return a and b
def or_gate(a, b):
    return a or b
def not_gate(a):
    return not a
if __name__ == '__main__':
    a_val = True
    b_val = False
    print("--- AND Gate ---")
    result_and = and_gate(a_val, b_val)
    print(f"A: {a_val}, B: {b_val}")
    print(f"A AND B: {result_and}")
    print("\n--- OR Gate ---")
    result_or = or_gate(a_val, b_val)
    print(f"A: {a_val}, B: {b_val}")
    print(f"A OR B: {result_or}")
    print("\n--- NOT Gate ---")
    result_not = not_gate(a_val)
    print(f"A: {a_val}")
    print(f"NOT A: {result_not}")