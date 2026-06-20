class TruthTableGenerator:
    def __init__(self):
        self.operations = {
            'AND': lambda x, y: x and y,
            'OR': lambda x, y: x or y,
            'NOT': lambda x: not x,
            'XOR': lambda x, y: x != y,
            'NAND': lambda x, y: not (x and y),
            'NOR': lambda x, y: not (x or y),
            'IMPLIES': lambda x, y: not x or y
        }

    def generate_truth_table(self, inputs):
        results = {}
        for bool1 in [True, False]:
            for bool2 in [True, False]:
                key = f"({bool1}, {bool2})"
                result = {op: self.operations[op](bool1, bool2) for op in self.operations}
                results[key] = result
        return results

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table([True, False])
    print(truth_table)