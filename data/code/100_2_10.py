class AndGate:
    GATE_NAME = "AND"
    NUM_INPUTS = 3

    def __init__(self, inputs):
        if len(inputs) != self.NUM_INPUTS:
            raise ValueError(f"Expected {self.NUM_INPUTS} inputs")
        self.inputs = tuple(int(bool(x)) for x in inputs)

    @staticmethod
    def compute(*args):
        if len(args) != AndGate.NUM_INPUTS:
            raise ValueError("Incorrect number of arguments")
        return 1 if all(args) else 0

    def evaluate(self):
        return self.compute(*self.inputs)

if __name__ == '__main__':
    gate_inputs = [1, 0, 1]
    gate = AndGate(gate_inputs)
    output = gate.evaluate()
    print(output)