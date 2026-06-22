class TruthTableGenerator:
    def __init__(self, num_inputs):
        if not isinstance(num_inputs, int) or num_inputs <= 0:
            raise ValueError("num_inputs must be a positive integer")
        self.num_inputs = num_inputs
        self.inputs = [chr(ord('A') + i) for i in range(num_inputs)]
        self.total_rows = 2 ** num_inputs

    def get_row(self, index):
        if index < 0 or index >= self.total_rows:
            raise ValueError("Index out of range")
        values = []
        for i in range(self.num_inputs):
            bit = (index >> (self.num_inputs - 1 - i)) & 1
            values.append(bool(bit))
        return values

    def compute_result(self, values):
        a, b, c, d = values
        return (a and b) or (c and d)

    def generate_table(self):
        table = []
        for i in range(self.total_rows):
            values = self.get_row(i)
            result = self.compute_result(values)
            row_dict = {inp: val for inp, val in zip(self.inputs, values)}
            row_dict['Result'] = result
            table.append(row_dict)
        return table

    def print_table(self, table):
        header = ' | '.join(f'{inp:<5}' for inp in self.inputs) + ' | Result'
        print(header)
        print('-' * len(header))
        for row in table:
            vals = [str(row[inp]) for inp in self.inputs]
            res = str(row['Result'])
            print(' | '.join(f'{v:<5}' for v in vals) + f' | {res}')

if __name__ == '__main__':
    generator = TruthTableGenerator(4)
    table = generator.generate_table()
    generator.print_table(table)
    first_row = generator.get_row(0)
    print(first_row)
    computed = generator.compute_result(first_row)
    print(computed)