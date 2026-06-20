class TruthTableGenerator:
    VARIABLES = ['A', 'B', 'C']
    
    @staticmethod
    def generate_header():
        return '|'.join(TruthTableGenerator.VARIABLES + ['Result'])
    
    @staticmethod
    def generate_separator(length):
        return '-' * (length - 1)
    
    def generate_truth_table(self):
        header = TruthTableGenerator.generate_header()
        separator = TruthTableGenerator.generate_separator(len(header))
        print(separator)
        print(header)
        print(separator)
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    result = self.evaluate_expression(a, b, c)
                    row = '|'.join([str(a), str(b), str(c), str(result)])
                    print(row)
                    print(separator)
    
    def evaluate_expression(self, a, b, c):
        return (a and b) or c

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()