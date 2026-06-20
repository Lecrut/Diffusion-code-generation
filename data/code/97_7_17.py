class TruthTableGenerator:
    def __init__(self, variables):
        self.variables = variables

    def generate_header(self):
        header = " | ".join(self.variables) + " | "
        for var in self.variables:
            header += f"{var} AND {var} | {var} OR {var} | NOT {var} | "
        return header.strip()

    def generate_truth_table_row(self, values):
        row = " | ".join(map(str, values)) + " | "
        for val in values:
            and_val = val and val
            or_val = val or val
            not_val = not val
            row += f"{and_val} | {or_val} | {not_val} | "
        return row.strip()

    def print_truth_table(self):
        header = self.generate_header()
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for i in range(2 ** len(self.variables)):
            values = [bool(i & (1 << j)) for j in range(len(self.variables))]
            row = self.generate_truth_table_row(values)
            print(row)

if __name__ == '__main__':
    generator = TruthTableGenerator(['P', 'Q'])
    generator.print_truth_table()