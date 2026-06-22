class LogicalAndTable:
    OPERANDS = [True, False]

    @staticmethod
    def _compute_result(val_a, val_b):
        return val_a and val_b

    @staticmethod
    def generate():
        rows = []
        for a in LogicalAndTable.OPERANDS:
            for b in LogicalAndTable.OPERANDS:
                rows.append((a, b, LogicalAndTable._compute_result(a, b)))
        return rows

if __name__ == '__main__':
    instance = LogicalAndTable()
    table_data = instance.generate()
    for row in table_data:
        print(row)