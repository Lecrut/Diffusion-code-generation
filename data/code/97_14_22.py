class OrTruthTableGenerator:
    def __init__(self, inputs=None):
        if inputs is None:
            inputs = [True, False]
        self.inputs = inputs

    def generate(self):
        table = []
        for p in self.inputs:
            for q in self.inputs:
                row = {"p": p, "q": q, "p | q": p | q}
                table.append(row)
        return table

    def get_row_count(self):
        return len(self.generate())

if __name__ == '__main__':
    generator = OrTruthTableGenerator()
    result = generator.generate()
    print(result)
    print(generator.get_row_count())