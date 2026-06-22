class LogicalANDTable:
    def __init__(self, inputs):
        self.inputs = inputs

    def compute_row(self, left, right):
        return left and right

    def generate(self):
        rows = []
        for left in self.inputs:
            for right in self.inputs:
                result = self.compute_row(left, right)
                rows.append((left, right, result))
        return rows

    def format_row(self, row):
        return f"{row[0]} AND {row[1]} = {row[2]}"

if __name__ == '__main__':
    sample_values = [True, False]
    table = LogicalANDTable(sample_values)
    rows = table.generate()
    for row in rows:
        print(table.format_row(row))