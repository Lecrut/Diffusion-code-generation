class XorTruthTableGenerator:
    INPUTS = [0, 1]

    @staticmethod
    def compute_xor(a, b):
        return a ^ b

    def generate(self):
        rows = []
        for a in self.INPUTS:
            for b in self.INPUTS:
                output = self.compute_xor(a, b)
                rows.append((a, b, output))
        return rows

if __name__ == '__main__':
    generator = XorTruthTableGenerator()
    table = generator.generate()
    for row in table:
        print(row)