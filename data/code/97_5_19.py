class TruthTableGenerator:
    def __init__(self, num_inputs=4):
        self.num_inputs = num_inputs
        self.input_names = [chr(ord('A') + i) for i in range(num_inputs)]
        self.total_rows = 2 ** num_inputs

    def get_row_values(self, index):
        values = []
        for i in range(self.num_inputs - 1, -1, -1):
            bit = (index >> i) & 1
            values.append(bool(bit))
        return values

    def compute_result(self, values):
        a, b, c, d = values
        return (a and b) or (c and d)

    def generate_table(self):
        table = []
        for i in range(self.total_rows):
            values = self.get_row_values(i)
            result = self.compute_result(values)
            row = {name: val for name, val in zip(self.input_names, values)}
            row['Result'] = result
            table.append(row)
        return table

    def print_table(self, table):
        header = ' | '.join(f'{name:<5}' for name in self.input_names + ['Result'])
        print(header)
        print('-' * len(header))
        for row in table:
            row_str = ' | '.join(f'{str(row[name]):<5}' for name in self.input_names + ['Result'])
            print(row_str)

if __name__ == '__main__':
    generator = TruthTableGenerator(4)
    table = generator.generate_table()
    generator.print_table(table)
    sample_row = table[0]
    print(sample_row['A'])
    print(sample_row['Result'])