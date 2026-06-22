class TruthTableGenerator:
    _VARIABLES = ['A', 'B', 'C']

    def __init__(self):
        self.variables = self._VARIABLES
        self.row_count = 2 ** len(self.variables)

    def _compute_logic(self, bits):
        return all(bits)

    def generate_table(self):
        header = ' | '.join(self.variables) + ' | Output'
        lines = [header]
        lines.append('-' * len(header))
        for i in range(self.row_count):
            bits = [(i >> (len(self.variables) - 1 - j)) & 1 for j in range(len(self.variables))]
            result = self._compute_logic(bits)
            row_str = ' | '.join(str(b) for b in bits) + ' | ' + str(result)
            lines.append(row_str)
        return '\n'.join(lines)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    table_output = generator.generate_table()
    print(table_output)