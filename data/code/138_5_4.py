import itertools

class TruthTableGenerator:
    def __init__(self):
        self.variables = ['A', 'B', 'C']

    def generate_truth_table(self):
        combinations = list(itertools.product([False, True], repeat=3))
        for combo in combinations:
            A, B, C = combo
            print(f"{A} {B} {C}")

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()