class LogicGates:
    @staticmethod
    def and_gate(A, B):
        return A & B

    @staticmethod
    def or_gate(A, B):
        return A | B

    @staticmethod
    def not_gate(A):
        return ~A + 2

    @staticmethod
    def nand_gate(A, B):
        return ~(A & B)

    @staticmethod
    def nor_gate(A, B):
        return ~(A | B)

    @staticmethod
    def xor_gate(A, B):
        return A ^ B

if __name__ == '__main__':
    logic = LogicGates()
    A_val = True
    B_val = False
    print(f"Inputs: A={A_val}, B={B_val}")
    print(f"AND: {logic.and_gate(int(A_val), int(B_val))}")
    print(f"OR: {logic.or_gate(int(A_val), int(B_val))}")
    print(f"NOT A: {logic.not_gate(int(A_val))}")
    print(f"NAND: {logic.nand_gate(int(A_val), int(B_val))}")
    print(f"NOR: {logic.nor_gate(int(A_val), int(B_val))}")
    print(f"XOR: {logic.xor_gate(int(A_val), int(B_val))}")