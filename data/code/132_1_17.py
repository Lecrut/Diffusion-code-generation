class LogicGate:
    def __init__(self):
        self.input_a = True
        self.input_b = False

    def nand(self):
        return not (self.input_a and self.input_b)

if __name__ == '__main__':
    gate = LogicGate()
    print(gate.nand())