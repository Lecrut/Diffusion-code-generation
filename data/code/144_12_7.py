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
            substitution = {}
            for k in range(n):
                substitution[variables[k]] = bool(row_values[k])
            substituted_formula = formula_str
            for var, val in substitution.items():
                substituted_formula = substituted_formula.replace(var, str(val))
            try:
                result = eval(substituted_formula)
                print(row_str + str(result))
            except Exception as e:
                print(row_str + "Error")
if __name__ == '__main__':
    solver = TruthTableSolver()
    formula1 = "(A & B)"
    variables1 = ["A", "B"]
    print("--- Truth Table for (A & B) ---")
    solver.generate_truth_table(formula1, variables1)
    print("\n" + "="*30 + "\n")
    formula2 = "(A | (B & C))"
    variables2 = ["A", "B", "C"]
    print("--- Truth Table for (A | (B & C)) ---")
    solver.generate_truth_table(formula2, variables2)
    print("\n" + "="*30 + "\n")
    formula3 = "(~A | (B & ~C))"
    variables3 = ["A", "B", "C"]
    print("--- Truth Table for (~A | (B & ~C)) ---")
    solver.generate_truth_table(formula3, variables3)