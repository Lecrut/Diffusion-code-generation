class ORTruthTable:
    def __init__(self, combinations):
        self.combinations = combinations

    def evaluate(self):
        return [[a, b, a or b] for a, b in self.combinations]

    def format_row(self, row):
        return f"{row[0]} | {row[1]} -> {row[2]}"

if __name__ == '__main__':
    inputs = [[True, False], [False, True], [True, True], [False, False]]
    table = ORTruthTable(inputs)
    results = table.evaluate()
    for row in results:
        print(table.format_row(row))