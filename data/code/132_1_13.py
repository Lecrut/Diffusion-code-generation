class LogicGate:
    INPUT_TRUE = True
    INPUT_FALSE = False

    @staticmethod
    def nand(a, b):
        return not (a and b)

if __name__ == '__main__':
    gate = LogicGate()
    print(gate.nand(LogicGate.INPUT_TRUE, LogicGate.INPUT_FALSE))