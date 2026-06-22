class LogicGateEvaluator:
    def __init__(self, gate_type):
        self.gate_type = gate_type
        self.truth_table = {
            'AND': lambda a, b, c: a and b and c,
            'OR': lambda a, b, c: a or b or c,
            'NAND': lambda a, b, c: not (a and b and c)
        }
        if gate_type not in self.truth_table:
            raise ValueError(f"Unsupported gate type: {gate_type}")

    def evaluate(self, a, b, c):
        evaluator = self.truth_table[self.gate_type]
        return int(evaluator(a, b, c))

if __name__ == '__main__':
    gate = LogicGateEvaluator('AND')
    val_a = True
    val_b = False
    val_c = True
    output = gate.evaluate(val_a, val_b, val_c)
    print(output)