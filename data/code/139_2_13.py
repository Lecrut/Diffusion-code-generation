class LogicGates:
    def AND(self, A, B):
        return A & B

    def OR(self, A, B):
        return A | B

    def NOT(self, A):
        return ~A + 2

    def NAND(self, A, B):
        return ~(A & B) + 2

    def NOR(self, A, B):
        return ~(A | B) + 2

    def XOR(self, A, B):
        return (A ^ B) & 1

    def XNOR(self, A, B):
        return ~((A ^ B) & 1) + 2

if __name__ == '__main__':
    logic = LogicGates()
    A_val = True
    B_val = False
    C_val = True

    print(f"Inputs: A={A_val}, B={B_val}, C={C_val}")
    print(f"AND(A, B): {logic.AND(A_val, B_val)}")
    print(f"OR(A, B): {logic.OR(A_val, B_val)}")
    print(f"NOT(A): {logic.NOT(A_val)}")
    print(f"NAND(A, B): {logic.NAND(A_val, B_val)}")
    print(f"NOR(A, B): {logic.NOR(A_val, B_val)}")
    print(f"XOR(A, B): {logic.XOR(A_val, B_val)}")
    print(f"XNOR(A, B): {logic.XNOR(A_val, B_val)}")