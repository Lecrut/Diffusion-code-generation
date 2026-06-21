class TruthTableEvaluator:
    EXPRESSION = "(A AND B) OR (NOT C)"
    
    @staticmethod
    def evaluate_expression(A, B, C):
        return (A and B) or (not C)
    
    @staticmethod
    def generate_truth_table():
        results = []
        for A in range(2):
            for B in range(2):
                for C in range(2):
                    result = TruthTableEvaluator.evaluate_expression(A, B, C)
                    results.append({'A': A, 'B': B, 'C': C, 'Result': result})
        return results

if __name__ == '__main__':
    table = TruthTableEvaluator.generate_truth_table()
    for row in table:
        print(row)