class TruthTable:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, a, b):
        return eval(self.expression, {'a': a, 'b': b})

    def display_table(self):
        print(f"{'A':<5}{'B':<5}{'Result':<10}")
        for a in [False, True]:
            for b in [False, True]:
                result = self.evaluate(a, b)
                print(f"{a:<5}{b:<5}{result:<10}")

if __name__ == '__main__':
    expression = "a and not b"
    table = TruthTable(expression)
    table.display_table()