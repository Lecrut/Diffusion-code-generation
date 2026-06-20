class NANDGate:
    def calculate(self, a, b):
        return not (a and b)

if __name__ == '__main__':
    nand = NANDGate()
    print(nand.calculate(True, True))
    print(nand.calculate(True, False))
    print(nand.calculate(False, True))
    print(nand.calculate(False, False))