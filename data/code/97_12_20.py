class TruthTable:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, val1, val2):
        return eval(self.expression.replace('a', str(val1)).replace('b', str(val2)))

    def generate_table(self):
        for a in [0, 1]:
            for b in [0, 1]:
                yield a, b, self.evaluate(a, b)

if __name__ == '__main__':
    table = TruthTable('a ^ b')
    for row in table.generate_table():
        print(row)