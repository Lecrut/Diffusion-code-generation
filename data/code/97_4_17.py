class TruthTableGenerator:
    def __init__(self):
        self.variables = ['A', 'B']

    def generate(self):
        table = []
        for i in range(4):
            a = (i >> 1) & 1
            b = i & 1
            table.append({self.variables[0]: bool(a), self.variables[1]: bool(b)})
        return table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    result = generator.generate()
    print(result)