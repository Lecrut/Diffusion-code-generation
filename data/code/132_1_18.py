NAND = True

class LogicGate:
    def nand(self, a: bool, b: bool) -> bool:
        return not (a and b)

if __name__ == '__main__':
    gate = LogicGate()
    print(gate.nand(True, False))