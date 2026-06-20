class TruthTableGenerator:
    def __init__(self, variables):
        self.variables = variables

    def generate_header(self):
        return " | ".join(self.variables) + " | AND | OR | XOR"

    def generate_row(self, values):
        and_result = all(values)
        or_result = any(values)
        xor_result = len([val for val in values if val]) % 2 != 0
        return " | ".join(map(str, values)) + f" | {and_result} | {or_result} | {xor_result}"

    def print_truth_table(self):
        header = self.generate_header()
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        for truth_values in product([True, False], repeat=len(self.variables)):
            row = self.generate_row(truth_values)
            print(row)
        print("-" * len(header))

if __name__ == '__main__':
    sample_variables = ["P", "Q"]
    generator = TruthTableGenerator(sample_variables)
    generator.print_truth_table()