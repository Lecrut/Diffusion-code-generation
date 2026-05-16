def and_gate(a, b):
    return a and b
def or_gate(a, b):
    return a or b
def not_gate(a):
    return not a
if __name__ == '__main__':
    a_in = True
    b_in = False
    print("--- AND Gate ---")
    result_and = and_gate(a_in, b_in)
    print(f"Input A: {a_in}, Input B: {b_in}")
    print(f"Result (A AND B): {result_and}")
    print("\n--- OR Gate ---")
    result_or = or_gate(a_in, b_in)
    print(f"Input A: {a_in}, Input B: {b_in}")
    print(f"Result (A OR B): {result_or}")
    print("\n--- NOT Gate ---")
    result_not = not_gate(a_in)
    print(f"Input A: {a_in}")
    print(f"Result (NOT A): {result_not}")