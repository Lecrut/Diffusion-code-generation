class TruthTableGenerator:
    OP_AND = "P AND Q"
    OP_OR = "P OR Q"
    OP_XOR = "P XOR Q"
    OP_NOT = "NOT P"
    OP_IMPLIES = "P IMPLIES Q"

    @staticmethod
    def compute_and(p, q):
        return p and q

    @staticmethod
    def compute_or(p, q):
        return p or q

    @staticmethod
    def compute_xor(p, q):
        return p ^ q

    @staticmethod
    def compute_not(p):
        return not p

    @staticmethod
    def compute_implies(p, q):
        return (not p) or q

    def generate_rows(self, inputs):
        rows = []
        for p, q in inputs:
            row = {
                'P': p,
                'Q': q,
                'P AND Q': self.compute_and(p, q),
                'P OR Q': self.compute_or(p, q),
                'P XOR Q': self.compute_xor(p, q),
                'NOT P': self.compute_not(p),
                'P IMPLIES Q': self.compute_implies(p, q),
            }
            rows.append(row)
        return rows

    def print_table(self, inputs):
        if not inputs:
            return

        headers = ['P', 'Q', 'P AND Q', 'P OR Q', 'P XOR Q', 'NOT P', 'P IMPLIES Q']
        widths = [5, 5, 10, 10, 10, 10, 15]

        header_line = "  ".join(f"{h:<{w}}" for h, w in zip(headers, widths))
        print(header_line)
        print("-" * (sum(widths) + len(widths) * 2 - 2))

        rows = self.generate_rows(inputs)
        for row in rows:
            values = [str(row[h]) for h in headers]
            line = "  ".join(f"{v:<{w}}" for v, w in zip(values, widths))
            print(line)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    sample_inputs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False),
    ]
    generator.print_table(sample_inputs)