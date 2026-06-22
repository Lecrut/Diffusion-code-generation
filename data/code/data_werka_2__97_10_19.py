class LogicalOperator:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def evaluate(self, p, q):
        return self.func(p, q)

class TruthTable:
    def __init__(self, operator):
        self.operator = operator
        self.rows = []

    def generate(self):
        self.rows = []
        values = [False, True]
        for p in values:
            for q in values:
                result = self.operator.evaluate(p, q)
                self.rows.append({'p': p, 'q': q, 'result': result})
        return self.rows

    def display(self):
        if not self.rows:
            self.generate()
        header = f"{'P':<5} | {'Q':<5} | {self.operator.name}"
        separator = "-" * len(header)
        print(header)
        print(separator)
        for row in self.rows:
            p_str = str(row['p'])
            q_str = str(row['q'])
            res_str = str(row['result'])
            line = f"{p_str:<5} | {q_str:<5} | {res_str}"
            print(line)

def main():
    and_op = LogicalOperator("AND", lambda p, q: p and q)
    table = TruthTable(and_op)
    table.generate()
    table.display()

if __name__ == '__main__':
    main()