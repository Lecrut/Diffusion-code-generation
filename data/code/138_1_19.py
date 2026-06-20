class NANDGate:
    def nand(self, a, b):
        return not (a and b)

if __name__ == '__main__':
    gate = NANDGate()
    print(gate.nand(True, True))
    print(gate.nand(True, False))
    print(gate.nand(False, True))
    print(gate.nand(False, False))