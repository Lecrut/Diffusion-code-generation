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
    formula = "(A AND B) OR (NOT A)"
    variables = ['A', 'B']
    print("Truth Table for formula: (A AND B) OR (NOT A)")
    solver.generate_truth_table(formula, variables)
    print("\n" + "="*30 + "\n")
    formula2 = "A OR B"
    variables2 = ['A', 'B']
    print("Truth Table for formula: A OR B")
    solver.generate_truth_table(formula2, variables2)