class ImplicationTruthTable:
    VARIABLES = [False, True]
    OPERATOR_SYMBOL = "->"
    HEADER_FORMAT = "P={:<5}Q={:<5}Result"

    @staticmethod
    def calculate_implication(p_val, q_val):
        if not isinstance(p_val, bool) or not isinstance(q_val, bool):
            raise ValueError("Arguments must be boolean")
        return (not p_val) or q_val

    def generate_rows(self):
        rows = []
        for p in self.VARIABLES:
            for q in self.VARIABLES:
                result = self.calculate_implication(p, q)
                rows.append((p, q, result))
        return rows

    @staticmethod
    def format_row(p, q, result):
        return f"P={p}, Q={q}, P {ImplicationTruthTable.OPERATOR_SYMBOL} Q={result}"

if __name__ == '__main__':
    table_gen = ImplicationTruthTable()
    rows = table_gen.generate_rows()
    for p, q, res in rows:
        formatted = ImplicationTruthTable.format_row(p, q, res)
        print(formatted)