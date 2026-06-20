class TruthTableGenerator:

    def generate_table(self):
        variables = ['A', 'B', 'C']
        header = ' | '.join(variables) + ' | Result'
        print(header)
        print('-' * len(header))
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    result = self.evaluate_expression(a, b, c)
                    row = f'{a} | {b} | {c} | {result}'
                    print(row)

    def evaluate_expression(self, a, b, c):
        return a and b or c
if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_table()