class TruthTableGenerator:
    HEADER_FORMAT = " | ".join(f"V{i+1}" for i in range(4))
    SEPARATOR = "-" * len(HEADER_FORMAT)

    @staticmethod
    def generate_truth_table(num_vars):
        num_rows = 2 ** num_vars
        if num_vars == 0:
            return [{"V1": False}]
        
        truth_table = []
        for i in range(num_rows):
            row_values = {}
            for j in range(num_vars):
                row_values[f"V{j+1}"] = (i >> j) & 1 > 0
            truth_table.append(row_values)
        
        return truth_table

if __name__ == '__main__':
    sample_outputs = TruthTableGenerator.generate_truth_table(2)
    for output in sample_outputs:
        print(output)