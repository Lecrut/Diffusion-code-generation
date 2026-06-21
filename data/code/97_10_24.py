class LogicalExpression:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def evaluate(self, p, q):
        return self.func(p, q)

class TruthTableGenerator:
    def __init__(self, expression):
        self.expression = expression

    def _get_combinations(self):
        return [
            (False, False),
            (False, True),
            (True, False),
            (True, True)
        ]

    def generate_rows(self):
        combinations = self._get_combinations()
        rows = []
        for p, q in combinations:
            result = self.expression.evaluate(p, q)
            rows.append({
                'P': p,
                'Q': q,
                'Result': result
            })
        return rows

    def format_table(self, rows):
        if not rows:
            return ""
        
        p_vals = [str(r['P']) for r in rows]
        q_vals = [str(r['Q']) for r in rows]
        res_vals = [str(r['Result']) for r in rows]
        
        p_width = max(len('P'), max(len(v) for v in p_vals))
        q_width = max(len('Q'), max(len(v) for v in q_vals))
        res_width = max(len('Result'), max(len(v) for v in res_vals))
        
        header = f"{'P':<{p_width}} | {'Q':<{q_width}} | {'Result':<{res_width}}"
        separator = f"{'-' * p_width}-+-{'-' * q_width}-+-{'-' * res_width}"
        
        lines = [header, separator]
        for r in rows:
            line = f"{str(r['P']):<{p_width}} | {str(r['Q']):<{q_width}} | {str(r['Result']):<{res_width}}"
            lines.append(line)
        
        return "\n".join(lines)

def main():
    def impl_and(p, q):
        return p and q

    def impl_or(p, q):
        return p or q

    def impl_nand(p, q):
        return not (p and q)

    expressions = {
        'AND': LogicalExpression('AND', impl_and),
        'OR': LogicalExpression('OR', impl_or),
        'NAND': LogicalExpression('NAND', impl_nand)
    }

    for name, expr in expressions.items():
        generator = TruthTableGenerator(expr)
        rows = generator.generate_rows()
        table_str = generator.format_table(rows)
        print(f"Truth Table for {name}")
        print(table_str)
        print()

if __name__ == '__main__':
    main()