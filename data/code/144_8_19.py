class TruthTableEvaluator:
    def __init__(self):
        self.variables = ['A', 'B', 'C', 'D']
    
    def generate_truth_table(self):
        num_rows = 2**len(self.variables)
        truth_table = []
        for i in range(num_rows):
            row_values = []
            for j in range(len(self.variables)):
                bit = (i >> j) & 1
                row_values.append(str(bit))
            truth_table.append(row_values)
        return truth_table
    
    def evaluate_expression(self, truth_table):
        results = []
        for row in truth_table:
            a, b, c, d = map(int, row)
            result = (a or b) and (c or d)
            results.append(result)
        return results

if __name__ == '__main__':
    evaluator = TruthTableEvaluator()
    truth_table = evaluator.generate_truth_table()
    results = evaluator.evaluate_expression(truth_table)
    for i, result in enumerate(results):
        print(f"Row {i+1}: {' '.join(evaluator.variables)} -> {result}")