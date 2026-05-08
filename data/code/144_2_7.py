class TruthTableSolver:
    def __init__(self, num_variables):
        self.num_variables = num_variables
    def generate_truth_table(self):
        num_rows = 2 ** self.num_variables
        results = []
        for i in range(num_rows):
            row_values = []
            temp = i
            for j in range(self.num_variables):
                bit = temp % 2
                row_values.append(str(bit))
                temp //= 2
            results.append(row_values)
        header = [f"V{j+1}" for j in range(self.num_variables)]
        table = [header]
        for row in results:
            table.append(row)
        return table
if __name__ == '__main__':
    num_vars = 3
    solver = TruthTableSolver(num_vars)
    truth_table = solver.generate_truth_table()
    print(f"Truth Table for {num_vars} variables:")
    header = [f"V{i+1}" for i in range(num_vars)]
    print(" | ".join(header))
    print("-" * (len(" | ".join(header)) + 3 * num_vars))
    for row in truth_table:
        print(" | ".join(row))