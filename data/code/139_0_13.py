def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return ~a + 2

def xor_gate(a, b):
    return a ^ b

def nand_gate(a, b):
    return ~(a & b) + 2

def nor_gate(a, b):
    return ~(a | b) + 2

def xnor_gate(a, b):
    return ~(a ^ b) + 2

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
    print(f"Input: {a_in}")
    print(f"Result (NOT A): {result_not}")
    
    print("\n--- XOR Gate ---")
    result_xor = xor_gate(a_in, b_in)
    print(f"Input A: {a_in}, Input B: {b_in}")
    print(f"Result (A XOR B): {result_xor}")
    
    print("\n--- NAND Gate ---")
    result_nand = nand_gate(a_in, b_in)
    print(f"Input A: {a_in}, Input B: {b_in}")
    print(f"Result (A NAND B): {result_nand}")
    
    print("\n--- NOR Gate ---")
    result_nor = nor_gate(a_in, b_in)
    print(f"Input A: {a_in}, Input B: {b_in}")
    print(f"Result (A NOR B): {result_nor}")
    
    print("\n--- XNOR Gate ---")
    result_xnor = xnor_gate(a_in, b_in)
    print(f"Input A: {a_in}, Input B: {b_in}")
    print(f"Result (A XNOR B): {result_xnor}")