class TruthTable:
    def __init__(self, expression, var1_values, var2_values):
        self.expression = expression
        self.var1_values = var1_values
        self.var2_values = var2_values
        self.results = []
    def evaluate(self, var1, var2):
        try:
            substituted_expression = self.expression.replace('V1', str(var1)).replace('V2', str(var2))
            result = eval(substituted_expression)
            return result
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            return None
    def generate_table(self):
        for v1 in self.var1_values:
            for v2 in self.var2_values:
                result = self.evaluate(v1, v2)
                self.results.append((v1, v2, result))
    def display(self):
        header = "V1 | V2 | Result\n"
        print("-" * len(header))
        for v1, v2, result in self.results:
            print(f"{v1} | {v2} | {result}")
        print("-" * len(header))
if __name__ == '__main__':
    expression = "(V1 AND V2) OR (NOT V1 AND NOT V2)"
    v1_values = [0, 1]
    v2_values = [0, 1]
    tt = TruthTable(expression, v1_values, v2_values)
    tt.generate_table()
    tt.display()