class TruthTableGenerator:
    def __init__(self):
        self.variables = ['A', 'B', 'C']
    
    def generate_truth_table(self):
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    print(f"{a} {b} {c}")

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()