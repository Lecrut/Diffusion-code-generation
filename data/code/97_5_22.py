class TruthTableGenerator:
    def __init__(self, num_inputs, expression_func):
        if not isinstance(num_inputs, int) or num_inputs <= 0:
            raise ValueError("num_inputs must be a positive integer")
        if not callable(expression_func):
            raise TypeError("expression_func must be callable")
        self.num_inputs = num_inputs
        self.expression_func = expression_func
        self.input_labels = [chr(ord('A') + i) for i in range(num_inputs)]

    def generate_rows(self):
        total_combinations = 2 ** self.num_inputs
        rows = []
        for i in range(total_combinations):
            input_values = []
            for j in range(self.num_inputs):
                bit = (i >> (self.num_inputs - 1 - j)) & 1
                input_values.append(bool(bit))
            result_val = self.expression_func(*input_values)
            row = {label: val for label, val in zip(self.input_labels, input_values)}
            row['Result'] = result_val
            rows.append(row)
        return rows

    def print_table(self):
        rows = self.generate_rows()
        header = ' | '.join(f'{label:<6}' for label in self.input_labels + ['Result'])
        print(header)
        print('-' * len(header))
        for row in rows:
            row_str = ' | '.join(f'{str(val):<6}' for val in row.values())
            print(row_str)

def my_logic(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    generator = TruthTableGenerator(4, my_logic)
    generator.print_table()