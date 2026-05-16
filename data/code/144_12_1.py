class TruthTableSolver:
    def generate_truth_table(self, formula_str, variables):
        n = len(variables)
        num_rows = 2**n
        header = " | ".join(variables)
        print(f"{header} |")
        for i in range(num_rows):
            row_values = []
            for j in range(n):
                if (i >> j) & 1:
                    row_values.append('T')
                else:
                    row_values.append('F')
            row_str = " | ".join(row_values)
            print(f"{row_str} |")
if __name__ == '__main__':
    solver = TruthTableSolver()
    formula = "(A AND B) OR (NOT A AND C)"
    variables = ['A', 'B', 'C']
    print("--- Truth Table for Formula: (A AND B) OR (NOT A AND C) ---")
    solver.generate_truth_table(formula, variables)
    print("\n--- Truth Table for Formula: A OR (B AND C) ---")
    formula2 = "A OR (B AND C)"
    variables2 = ['A', 'B', 'C']
    solver.generate_truth_table(formula2, variables2)