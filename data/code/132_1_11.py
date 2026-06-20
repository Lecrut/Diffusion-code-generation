class LogicGate:

    def nand(self, a, b):
        return not (a and b)
if __name__ == '__main__':
    gate = LogicGate()
    result1 = gate.nand(True, False)
    print(result1)
    result2 = gate.nand(False, True)
    print(result2)
    result3 = gate.nand(True, True)
    print(result3)
    result4 = gate.nand(False, False)
    print(result4)