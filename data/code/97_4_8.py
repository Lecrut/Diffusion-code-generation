class TruthTableBuilder:
    def __init__(self, variable_count=2):
        self.validate_count(variable_count)
        self.variable_count = variable_count

    def validate_count(self, count):
        if not isinstance(count, int) or count < 1:
            raise ValueError("Variable count must be a positive integer")

    def build(self):
        rows = []
        limit = 1 << self.variable_count
        for i in range(limit):
            row = []
            for j in range(self.variable_count - 1, -1, -1):
                row.append((i >> j) & 1)
            rows.append(tuple(row))
        return rows

if __name__ == '__main__':
    builder = TruthTableBuilder(2)
    table = builder.build()
    print(table)