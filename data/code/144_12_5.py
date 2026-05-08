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
def solve():
    solver = TruthTableSolver()
    formula = "A AND B"
    variables = ["A", "B"]
    print(f"Evaluating formula: {formula} for variables: {variables}\n")
    solver.generate_truth_table(formula, variables)
if __name__ == '__main__':
    solve()