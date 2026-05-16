class TruthTable:
    def __init__(self, expression, var1_values, var2_values):
        self.expression = expression
        self.var1_values = var1_values
        self.var2_values = var2_values
        self.results = []
    def evaluate(self, var1, var2):
        try:
            result = eval(self.expression, {"__builtins__": None}, {"var1": var1, "var2": var2})
            return str(result)
        except Exception as e:
            return f"Error: {e}"
    def generate_table(self):
        for v1 in self.var1_values:
            for v2 in self.var2_values:
                result = self.evaluate(v1, v2)
                self.results.append((v1, v2, result))
    def display(self):
        header = "Var1 | Var2 | Result\n"
        print(header)
        for v1, v2, res in self.results:
            print(f"{v1}   | {v2}   | {res}")
if __name__ == '__main__':
    expression = "(var1 AND var2) OR (NOT var1 AND NOT var2)"
    var1_values = [0, 1]
    var2_values = [0, 1]
    tt = TruthTable(expression, var1_values, var2_values)
    tt.generate_table()
    tt.display()