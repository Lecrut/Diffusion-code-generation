class TruthTableGenerator:
    def generate_truth_table(self, inputs):
        if not isinstance(inputs, list) or len(inputs) != 2:
            return "Error: Input must be a list of exactly two boolean values."
        
        num_rows = 2 ** len(inputs)
        table = []
        
        for i in range(num_rows):
            row = {}
            for j, input_val in enumerate(inputs):
                row[f'a{j+1}'] = str(input_val if (i >> j) & 1 else not input_val)
            row['result'] = str(row['a1'] == row['a2'])
            table.append(row)
        
        return table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table([True, False])
    print(truth_table)