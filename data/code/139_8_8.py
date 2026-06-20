class LogicGates:
    def AND(self, a, b):
        return a & b
    
    def OR(self, a, b):
        return a | b
    
    def NOT(self, a):
        return ~a + 2
    
    def XOR(self, a, b):
        return a ^ b
    
    def NAND(self, a, b):
        return ~(a & b) + 1
    
    def NOR(self, a, b):
        return ~(a | b) + 1
    
    def XNOR(self, a, b):
        return ~(a ^ b) + 1

if __name__ == '__main__':
    gates = LogicGates()
    
    print("--- AND Gate Demonstration ---")
    print(f"AND(0, 0) = {gates.AND(0, 0)}")
    print(f"AND(0, 1) = {gates.AND(0, 1)}")
    print(f"AND(1, 0) = {gates.AND(1, 0)}")
    print(f"AND(1, 1) = {gates.AND(1, 1)}")
    
    print("--- OR Gate Demonstration ---")
    print(f"OR(0, 0) = {gates.OR(0, 0)}")
    print(f"OR(0, 1) = {gates.OR(0, 1)}")
    print(f"OR(1, 0) = {gates.OR(1, 0)}")
    print(f"OR(1, 1) = {gates.OR(1, 1)}")
    
    print("--- NOT Gate Demonstration ---")
    print(f"NOT(0) = {gates.NOT(0)}")
    print(f"NOT(1) = {gates.NOT(1)}")
    
    print("--- XOR Gate Demonstration ---")
    print(f"XOR(0, 0) = {gates.XOR(0, 0)}")
    print(f"XOR(0, 1) = {gates.XOR(0, 1)}")
    print(f"XOR(1, 0) = {gates.XOR(1, 0)}")
    print(f"XOR(1, 1) = {gates.XOR(1, 1)}")
    
    print("--- NAND Gate Demonstration ---")
    print(f"NAND(0, 0) = {gates.NAND(0, 0)}")
    print(f"NAND(0, 1) = {gates.NAND(0, 1)}")
    print(f"NAND(1, 0) = {gates.NAND(1, 0)}")
    print(f"NAND(1, 1) = {gates.NAND(1, 1)}")
    
    print("--- NOR Gate Demonstration ---")
    print(f"NOR(0, 0) = {gates.NOR(0, 0)}")
    print(f"NOR(0, 1) = {gates.NOR(0, 1)}")
    print(f"NOR(1, 0) = {gates.NOR(1, 0)}")
    print(f"NOR(1, 1) = {gates.NOR(1, 1)}")
    
    print("--- XNOR Gate Demonstration ---")
    print(f"XNOR(0, 0) = {gates.XNOR(0, 0)}")
    print(f"XNOR(0, 1) = {gates.XNOR(0, 1)}")
    print(f"XNOR(1, 0) = {gates.XNOR(1, 0)}")
    print(f"XNOR(1, 1) = {gates.XNOR(1, 1)}")