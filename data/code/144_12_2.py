class TruthTableSolver:
    def generate_truth_table(self, formula, variables):
        n = len(variables)
        num_rows = 2**n
        header = [""] + variables
        print(f"{header[0]:<10} | {' | '.join(header[1:])}")
        print("-" * (10 + 3 * n + 3 * (n * (n - 1) // 2)))
        for i in range(num_rows):
            row_values = []
            for j in range(n):
                if (i >> j) & 1:
                    row_values.append('T')
                else:
                    row_values.append('F')
            print(f"{row_values[0]:<10} | {' | '.join(row_values[1:])}")
if __name__ == '__main__':
    solver = TruthTableSolver()
    formula1 = "A & B"
    variables1 = ["A", "B"]
    print("--- Truth Table for A & B ---")
    solver.generate_truth_table(formula1, variables1)
    print("\n" + "="*30 + "\n")
    formula2 = "(A & B) | C"
    variables2 = ["A", "B", "C"]
    print("--- Truth Table for (A & B) | C ---")
    solver.generate_truth_table(formula2, variables2)
    print("\n" + "="*30 + "\n")
    formula3 = "A & B & C & D"
    variables3 = ["A", "B", "C", "D"]
    print("--- Truth Table for A & B & C & D ---")
    solver.generate_truth_table(formula3, variables3)