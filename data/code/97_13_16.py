class LogicalAndTable:
    OPERANDS = [True, False]

    @staticmethod
    def compute(a, b):
        return a and b

    @staticmethod
    def generate():
        rows = []
        for a in LogicalAndTable.OPERANDS:
            for b in LogicalAndTable.OPERANDS:
                result = LogicalAndTable.compute(a, b)
                rows.append((a, b, result))
        return rows

if __name__ == '__main__':
    table_instance = LogicalAndTable()
    rows = table_instance.generate()
    for row in rows:
        print(row)