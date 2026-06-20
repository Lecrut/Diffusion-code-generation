class LogicGates:
    def AND(self, a, b):
        return a & b
    
    def OR(self, a, b):
        return a | b
    
    def NOT(self, a):
        return not a
    
    def XOR(self, a, b):
        return a ^ b
    
    def NAND(self, a, b):
        return not a & b
    
    def NOR(self, a, b):
        return not a | b
    
    def XNOR(self, a, b):
        return not a ^ b

if __name__ == '__main__':
    logic = LogicGates()
    print(logic.AND(True, False))
    print(logic.OR(False, True))
    print(logic.NOT(True))