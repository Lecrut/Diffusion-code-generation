class TruthTableSolver:
    def generate_truth_table(self, formula, variables):
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
    formula = "A AND B"
    variables = ["A", "B"]
    print("Truth Table for A AND B:")
    solver.generate_truth_table(formula, variables)
    print("\nTruth Table for (A OR B) AND NOT A:")
    formula2 = "(A OR B) AND NOT A"
    variables2 = ["A", "B"]
    solver.generate_truth_table(formula2, variables2)