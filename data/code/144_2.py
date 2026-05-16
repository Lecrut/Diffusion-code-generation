class TruthTableSolver:
    def __init__(self, num_variables):
        self.num_variables = num_variables
    def generate_truth_table(self):
        num_rows = 2 ** self.num_variables
        results = []
        for i in range(num_rows):
            row = []
            for j in range(self.num_variables):
                bit = (i >> j) & 1
                row.append(str(bit))
            results.append(row)
        return results
if __name__ == '__main__':
    num_vars = 3
    solver = TruthTableSolver(num_vars)
    truth_table = solver.generate_truth_table()
    for row in truth_table:
        print(" ".join(row))