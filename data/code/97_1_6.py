class TruthTableGenerator:
    _VAR_NAMES = ('A', 'B', 'C')
    _OPERATORS = {
        'AND': lambda a, b, c: a and b and c,
        'OR': lambda a, b, c: a or b or c,
        'XOR': lambda a, b, c: a ^ b ^ c,
        'NAND': lambda a, b, c: not (a and b and c),
    }

    def __init__(self, operation='AND'):
        if operation not in self._OPERATORS:
            raise ValueError(f"Unsupported operation: {operation}")
        self._operation = operation
        self._func = self._OPERATORS[operation]

    def _format_row(self, vals):
        parts = [str(int(v)) for v in vals]
        return ' | '.join(parts)

    def generate_table(self):
        header = ' | '.join(self._VAR_NAMES) + ' | Result'
        lines = [header, '-' * len(header)]
        
        for i in range(8):
            a = (i >> 2) & 1
            b = (i >> 1) & 1
            c = (i >> 0) & 1
            result = self._func(bool(a), bool(b), bool(c))
            
            row_vals = [a, b, c, int(result)]
            row_str = self._format_row(row_vals)
            lines.append(row_str)
            
        return '\n'.join(lines)

if __name__ == '__main__':
    gen = TruthTableGenerator('AND')
    print(gen.generate_table())