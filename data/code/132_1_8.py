class LogicGate:
    def __init__(self):
        self.input_a = True
        self.input_b = False

    def nand(self, a=None, b=None):
        if a is None and b is None:
            a = self.input_a
            b = self.input_b
        return not (a and b)

if __name__ == '__main__':
    gate = LogicGate()
    print(gate.nand())