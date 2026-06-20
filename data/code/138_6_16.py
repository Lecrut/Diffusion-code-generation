class BooleanTableGenerator:
    def __init__(self):
        self.variables = ['A', 'B']
    
    def generate_truth_table(self):
        truth_table = []
        for a in [False, True]:
            for b in [False, True]:
                implication_result = not a or b
                equivalence_result = a == b
                truth_table.append((a, b, implication_result, equivalence_result))
        return truth_table

if __name__ == '__main__':
    generator = BooleanTableGenerator()
    table = generator.generate_truth_table()
    for row in table:
        print(row)