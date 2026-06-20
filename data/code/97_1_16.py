class TruthTableGenerator:

    def generate_truth_table(self):
        variables = ['A', 'B', 'C']
        header = '|'.join(variables + ['Result'])
        separator = '-' * (len(header) - 1)
        print(separator)
        print(header)
        print(separator)
        for a in [0, 1]:
            for b in [0, 1]:
                for c in [0, 1]:
                    result = self.evaluate_expression(a, b, c)
                    row = '|'.join([str(a), str(b), str(c), str(result)])
                    print(row)
        print(separator)

    def evaluate_expression(self, a, b, c):
        return a and b or c
if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()