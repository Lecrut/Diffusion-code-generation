class TruthTableGenerator:
    def generate_truth_table(self, var_names):
        table = []
        n_vars = len(var_names)
        for i in range(2 ** n_vars):
            row = []
            for j in range(n_vars):
                row.append((i >> j) & 1)
            table.append(row)
        return table

    def format_truth_table(self, var_names, truth_table):
        header = [''] + var_names
        rows = [header]
        for row in truth_table:
            formatted_row = [str(val) for val in row]
            rows.append(formatted_row)
        return rows

if __name__ == '__main__':
    generator = TruthTableGenerator()
    variables = ["A", "B", "C", "D"]
    truth_table = generator.generate_truth_table(variables)
    formatted_table = generator.format_truth_table(variables, truth_table)
    for row in formatted_table:
        print(row)