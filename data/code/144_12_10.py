class TruthTableSolver:
    def generate_truth_table(self, formula, variables):
        n = len(variables)
        num_rows = 2**n
        header = [f"| {variables[0]} | {variables[1]} | ... |"]
        header_parts = []
        for var in variables:
            header_parts.append(f"{var}")
        header.append(" | ".join(header_parts))
        print(header)
        print("-" * len(header))
        for i in range(num_rows):
            row_values = []
            for j in range(n):
                if (i >> j) & 1:
                    row_values.append('T')
                else:
                    row_values.append('F')
            row_str = " | ".join(row_values)
            assignment = {}
            for k in range(n):
                assignment[variables[k]] = row_values[k]
            try:
                result = eval(formula, {}, assignment)
                row_str += f" | {result}"
            except Exception as e:
                row_str += " | Error"
            print(row_str)
truth_table = TruthTableSolver()
formula1 = "(A AND B) OR (NOT A AND B)"
variables1 = ['A', 'B']
print("Truth Table for Formula 1:")
truth_table.generate_truth_table(formula1, variables1)
print("\n" + "="*30 + "\n")
formula2 = "(A OR B) AND (NOT A OR NOT B)"
variables2 = ['A', 'B']
print("Truth Table for Formula 2:")
truth_table.generate_truth_table(formula2, variables2)
if __name__ == '__main__':
    pass