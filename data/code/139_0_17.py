class LogicGates:
    @staticmethod
    def and_gate(a: bool, b: bool) -> bool:
        return a & b

    @staticmethod
    def or_gate(a: bool, b: bool) -> bool:
        return a | b

    @staticmethod
    def not_gate(a: bool) -> bool:
        return ~a & 1

    @staticmethod
    def xor_gate(a: bool, b: bool) -> bool:
        return (a & ~b) | (~a & b)

    @staticmethod
    def nand_gate(a: bool, b: bool) -> bool:
        return ~(a & b)

    @staticmethod
    def nor_gate(a: bool, b: bool) -> bool:
        return ~(a | b)

    @staticmethod
    def xnor_gate(a: bool, b: bool) -> bool:
        return ~(a ^ b)

if __name__ == '__main__':
    gate = LogicGates()
    A = True
    B = False

    print("--- AND Gate ---")
    result_and = gate.and_gate(A, B)
    print(f"A: {A}, B: {B}")
    print(f"A AND B: {result_and}")

    print("\n--- OR Gate ---")
    result_or = gate.or_gate(A, B)
    print(f"A: {A}, B: {B}")
    print(f"A OR B: {result_or}")

    print("\n--- NOT Gate ---")
    result_not = gate.not_gate(A)
    print(f"NOT A: {result_not}")

    print("\n--- XOR Gate ---")
    result_xor = gate.xor_gate(A, B)
    print(f"A: {A}, B: {B}")
    print(f"A XOR B: {result_xor}")

    print("\n--- NAND Gate ---")
    result_nand = gate.nand_gate(A, B)
    print(f"A: {A}, B: {B}")
    print(f"A NAND B: {result_nand}")

    print("\n--- NOR Gate ---")
    result_nor = gate.nor_gate(A, B)
    print(f"A: {A}, B: {B}")
    print(f"A NOR B: {result_nor}")

    print("\n--- XNOR Gate ---")
    result_xnor = gate.xnor_gate(A, B)
    print(f"A: {A}, B: {B}")
    print(f"A XNOR B: {result_xnor}")