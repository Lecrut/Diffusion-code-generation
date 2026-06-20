def and_gate(a, b):
    return bool(a & b)

def or_gate(a, b):
    return bool(a | b)

def not_gate(a):
    return bool(~a)

def xor_gate(a, b):
    return bool(a ^ b)

def nand_gate(a, b):
    return bool(~(a & b))

def nor_gate(a, b):
    return bool(~(a | b))

def xnor_gate(a, b):
    return bool(~(a ^ b))

if __name__ == '__main__':
    a = True
    b = False
    print("--- AND Gate ---")
    print(f"Input A: {a}, Input B: {b}")
    print(f"Result (A AND B): {and_gate(a, b)}")
    
    print("\n--- OR Gate ---")
    print(f"Input A: {a}, Input B: {b}")
    print(f"Result (A OR B): {or_gate(a, b)}")
    
    print("\n--- NOT Gate ---")
    print(f"Input A: {a}")
    print(f"Result (NOT A): {not_gate(a)}")
    
    print("\n--- XOR Gate ---")
    print(f"Input A: {a}, Input B: {b}")
    print(f"Result (A XOR B): {xor_gate(a, b)}")
    
    print("\n--- NAND Gate ---")
    print(f"Input A: {a}, Input B: {b}")
    print(f"Result (A NAND B): {nand_gate(a, b)}")
    
    print("\n--- NOR Gate ---")
    print(f"Input A: {a}, Input B: {b}")
    print(f"Result (A NOR B): {nor_gate(a, b)}")
    
    print("\n--- XNOR Gate ---")
    print(f"Input A: {a}, Input B: {b}")
    print(f"Result (A XNOR B): {xnor_gate(a, b)}")