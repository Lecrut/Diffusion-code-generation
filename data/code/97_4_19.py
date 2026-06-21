class BinaryTruthTable:
    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError("variables must be a list")
        if len(variables) != 2:
            raise ValueError("exactly two variables required")
        self.var_names = variables
        self.num_vars = 2

    def compute_rows(self):
        combinations = []
        limit = 1 << self.num_vars
        for idx in range(limit):
            current_row = []
            temp_val = idx
            for _ in range(self.num_vars):
                bit = temp_val & 1
                current_row.insert(0, bit)
                temp_val >>= 1
            combinations.append(current_row)
        return combinations

    def format_table(self):
        rows = self.compute_rows()
        header = " | ".join(self.var_names)
        lines = [header]
        lines.append("-" * len(header))
        for row in rows:
            line = " | ".join(str(val) for val in row)
            lines.append(line)
        return "\n".join(lines)

if __name__ == '__main__':
    table_generator = BinaryTruthTable(["x", "y"])
    formatted_output = table_generator.format_table()
    print(formatted_output)