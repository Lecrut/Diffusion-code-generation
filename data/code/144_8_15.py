class TruthTableEvaluator:
    VARIABLES = ['A', 'B', 'C', 'D']
    EXPRESSION = "(A OR B) AND (C OR D)"

    @staticmethod
    def generate_truth_table():
        num_vars = len(TruthTableEvaluator.VARIABLES)
        num_rows = 2 ** num_vars
        truth_table = []
        for i in range(num_rows):
            row = {var: str((i >> j) & 1) for j, var in enumerate(TruthTableEvaluator.VARIABLES)}
            truth_table.append(row)
        return truth_table

    @staticmethod
    def evaluate_expression(variables):
        A, B, C, D = variables['A'], variables['B'], variables['C'], variables['D']
        result = (A or B) and (C or D)
        return result

if __name__ == '__main__':
    evaluator = TruthTableEvaluator()
    truth_table = evaluator.generate_truth_table()
    for row in truth_table:
        print(row, "Result:", evaluator.evaluate_expression(row))