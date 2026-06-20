class LogicGate:
    def __init__(self):
        self.input1 = True
        self.input2 = False

    def nand(self):
        return not (self.input1 and self.input2)

if __name__ == '__main__':
    gate = LogicGate()
    print(gate.nand())