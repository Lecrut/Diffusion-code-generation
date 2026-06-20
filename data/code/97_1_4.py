class TruthTableGenerator:
    def generate_truth_table(self):
        variables = ['A', 'B', 'C']
        header = '|'.join(variables) + '|'
        separator = '-' * len(header)
        
        print(separator)
        print(header)
        print(separator)
        
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    row = f"{a}|{b}|{c}"
                    print(row)
                    print(separator)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()