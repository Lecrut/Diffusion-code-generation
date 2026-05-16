class TruthTable:
    def __init__(self, expression, var1_name, var2_name):
        self.expression = expression
        self.var1_name = var1_name
        self.var2_name = var2_name
        self.results = []
    def evaluate(self, val1, val2):
        try:
            substituted_expression = self.expression.replace(self.var1_name, str(val1)).replace(self.var2_name, str(val2))
            result = eval(substituted_expression)
            return result
        except Exception as e:
            return f"Error evaluating: {e}"
    def generate_table(self):
        values1 = [0, 1]
        values2 = [0, 1]
        for v1 in values1:
            for v2 in values2:
                result = self.evaluate(v1, v2)
                self.results.append((v1, v2, result))
    def display(self):
        header = f"{self.var1_name}\t{self.var2_name}\t{self.expression}"
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        for v1, v2, result in self.results:
            print(f"{v1}\t{v2}\t{result}")
if __name__ == '__main__':
    expression = "(A and B) or (not A and B)"
    var1 = "A"
    var2 = "B"
    tt = TruthTable(expression, var1, var2)
    tt.generate_table()
    tt.display()