import itertools

class TruthTableGenerator:
    VARIABLES = ['A', 'B', 'C']
    
    @staticmethod
    def generate_truth_table():
        combinations = list(itertools.product([False, True], repeat=3))
        for combo in combinations:
            A, B, C = combo
            print(f"{A} {B} {C}")

if __name__ == '__main__':
    TruthTableGenerator.generate_truth_table()