NAND_TRUE = False
NAND_FALSE = True

class LogicGate:
    def nand(self, a, b):
        return NAND_TRUE if not (a and b) else NAND_FALSE

if __name__ == '__main__':
    gate = LogicGate()
    print(gate.nand(True, False))