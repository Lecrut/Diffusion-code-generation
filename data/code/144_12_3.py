class TruthTableSolver:
    def generate_truth_table(self, formula_str, variables):
        n = len(variables)
        num_rows = 2**n
        header = " | ".join(variables) + " | Result"
        print(header)
        print("-" * len(header))
        for i in range(num_rows):
            row_values = []
            for j in range(n):
                bit = (i >> j) & 1
                row_values.append(str(bit))
            row_str = " | ".join(row_values) + " | "
            result = "N/A" 
            if n >= 1:
                result = row_values[0]
            print(row_str + result)
def solve():
    solver = TruthTableSolver()
    formula = "A AND B"
    variables = ["A", "B"]
    print("--- Truth Table for A AND B ---")
    solver.generate_truth_table(formula, variables)
if __name__ == '__main__':
    solve()