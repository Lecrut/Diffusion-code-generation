class TruthTableGenerator:
    VARIABLES = ['A', 'B', 'C']
    HEADER = '|'.join(VARIABLES + ['Result'])
    SEPARATOR = '-' * (len(HEADER) - 1)

    def generate_truth_table(self):
        print(self.SEPARATOR)
        print(self.HEADER)
        print(self.SEPARATOR)
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    result = self.evaluate_expression(a, b, c)
                    row = '|'.join([str(a), str(b), str(c), str(result)])
                    print(row)
                    print(self.SEPARATOR)

    def evaluate_expression(self, a, b, c):
        return (a and b) or c

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()