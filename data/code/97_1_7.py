class TruthTableGenerator:
    def __init__(self):
        self.variables = ['A', 'B', 'C']
        self.logic_function = lambda a, b, c: (a or b) and (not c)

    def _get_bits(self, n, count):
        bits = []
        for k in range(count - 1, -1, -1):
            bit = (n >> k) & 1
            bits.append(bool(bit))
        return bits

    def generate(self):
        num_vars = len(self.variables)
        total_rows = 2 ** num_vars
        table_data = []
        for i in range(total_rows):
            values = self._get_bits(i, num_vars)
            result = self.logic_function(*values)
            table_data.append((values, result))
        return table_data

    def format_table(self, data):
        num_vars = len(self.variables)
        header = ' | '.join(self.variables) + ' | Result'
        lines = [header]
        lines.append('-' * len(header))
        for values, result in data:
            value_strs = [str(int(v)) for v in values]
            result_str = str(int(result))
            row = ' | '.join(value_strs) + ' | ' + result_str
            lines.append(row)
        return '\n'.join(lines)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    data = generator.generate()
    table = generator.format_table(data)
    print(table)