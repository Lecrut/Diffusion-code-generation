class LogicalExpressionEvaluator:
    VARIABLES = ['P', 'Q']
    OPERATIONS = {
        'AND': lambda p, q: p and q,
        'OR': lambda p, q: p or q,
        'NAND': lambda p, q: not (p and q),
        'NOR': lambda p, q: not (p or q),
        'XOR': lambda p, q: p ^ q,
        'IMPLIES': lambda p, q: (not p) or q
    }

    def __init__(self, operation_name):
        if operation_name not in self.OPERATIONS:
            raise ValueError(f"Unsupported operation: {operation_name}")
        self.operation_name = operation_name
        self.operation_func = self.OPERATIONS[operation_name]

    def evaluate(self, p_val, q_val):
        return self.operation_func(p_val, q_val)

    def generate_rows(self):
        rows = []
        for p in [False, True]:
            for q in [False, True]:
                res = self.evaluate(p, q)
                rows.append((p, q, res))
        return rows

    def format_table(self):
        rows = self.generate_rows()
        header = f"{self.VARIABLES[0]:<5} | {self.VARIABLES[1]:<5} | {self.operation_name:<5}"
        separator = "-" * len(header)
        lines = [header, separator]
        for p, q, res in rows:
            line = f"{str(p):<5} | {str(q):<5} | {str(res):<5}"
            lines.append(line)
        return "\n".join(lines)

if __name__ == '__main__':
    evaluator = LogicalExpressionEvaluator('AND')
    print(evaluator.format_table())