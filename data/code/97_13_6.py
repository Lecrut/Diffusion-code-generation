class AndTruthTable:
    def __init__(self, inputs):
        self.inputs = inputs

    def generate(self):
        if not self.inputs:
            return []
        return [
            (a, b, a and b)
            for a in self.inputs
            for b in self.inputs
        ]

if __name__ == '__main__':
    sample_values = [True, False]
    table = AndTruthTable(sample_values)
    rows = table.generate()
    for row in rows:
        print(row)