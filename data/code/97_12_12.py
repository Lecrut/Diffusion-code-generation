class TruthTable:
    VAR1 = 'var1'
    VAR2 = 'var2'
    
    @staticmethod
    def evaluate(expression, var1, var2):
        return eval(expression, {'__builtins__': None}, {TruthTable.VAR1: var1, TruthTable.VAR2: var2})
    
    def generate_table(self):
        results = []
        for val1 in [0, 1]:
            for val2 in [0, 1]:
                result = self.evaluate("var1 ^ var2", val1, val2)
                results.append((val1, val2, result))
        return results

if __name__ == '__main__':
    truth_table = TruthTable()
    table = truth_table.generate_table()
    for row in table:
        print(row)