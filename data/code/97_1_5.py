class TruthTableGenerator:
    def generate_truth_table(self):
        variables = ['A', 'B', 'C']
        header = '|'.join(variables) + '|'
        separator = '-' * len(header)
        
        print(separator)
        print(header)
        print(separator)
        
        for a in [0, 1]:
            for b in [0, 1]:
                for c in [0, 1]:
                    row = f"{a}|{b}|{c}"
                    print(row)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()