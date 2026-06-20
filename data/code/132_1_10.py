class LogicGate:
    def nand(self, a: bool, b: bool) -> bool:
        return not (a and b)

if __name__ == '__main__':
    gate = LogicGate()
    print(gate.nand(True, False))
    print(gate.nand(False, True))
    print(gate.nand(True, True))
    print(gate.nand(False, False))