class LogicGates:
    def and_gate(self, a: bool, b: bool) -> bool:
        return a & b

    def or_gate(self, a: bool, b: bool) -> bool:
        return a | b

    def not_gate(self, a: bool) -> bool:
        return ~a & 1

    def xor_gate(self, a: bool, b: bool) -> bool:
        return a ^ b

    def nand_gate(self, a: bool, b: bool) -> bool:
        return ~(a & b)

    def nor_gate(self, a: bool, b: bool) -> bool:
        return ~(a | b)

    def xnor_gate(self, a: bool, b: bool) -> bool:
        return ~(a ^ b)

if __name__ == '__main__':
    logic = LogicGates()
    print("--- AND Gate ---")
    result_and = logic.and_gate(True, False)
    print(f"Input A: True, Input B: False")
    print(f"Result (A AND B): {result_and}")
    
    print("\n--- OR Gate ---")
    result_or = logic.or_gate(True, False)
    print(f"Input A: True, Input B: False")
    print(f"Result (A OR B): {result_or}")
    
    print("\n--- NOT Gate ---")
    result_not = logic.not_gate(True)
    print(f"Input A: True")
    print(f"Result (NOT A): {result_not}")
    
    print("\n--- XOR Gate ---")
    result_xor = logic.xor_gate(True, False)
    print(f"Input A: True, Input B: False")
    print(f"Result (A XOR B): {result_xor}")
    
    print("\n--- NAND Gate ---")
    result_nand = logic.nand_gate(True, False)
    print(f"Input A: True, Input B: False")
    print(f"Result (A NAND B): {result_nand}")
    
    print("\n--- NOR Gate ---")
    result_nor = logic.nor_gate(True, False)
    print(f"Input A: True, Input B: False")
    print(f"Result (A NOR B): {result_nor}")
    
    print("\n--- XNOR Gate ---")
    result_xnor = logic.xnor_gate(True, False)
    print(f"Input A: True, Input B: False")
    print(f"Result (A XNOR B): {result_xnor}")