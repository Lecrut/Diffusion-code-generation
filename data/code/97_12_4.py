class TruthTable:
    def __init__(self, expression, var1_name, var2_name):
        self.expression = expression
        self.var1_name = var1_name
        self.var2_name = var2_name
        self.results = []
    def evaluate(self, val1, val2):
        try:
            temp_expression = self.expression.replace(self.var1_name, str(val1)).replace(self.var2_name, str(val2))
            result = eval(temp_expression)
            return result
        except Exception as e:
            return f"Error evaluating: {e}"
    def generate(self):
        values1 = [0, 1]
        values2 = [0, 1]
        for v1 in values1:
            for v2 in values2:
                result = self.evaluate(v1, v2)
                self.results.append((v1, v2, result))
    def display(self):
        header = f"{self.var1_name}\t{self.var2_name}\tResult"
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        for v1, v2, res in self.results:
            print(f"{v1}\t{v2}\t{res}")
if __name__ == '__main__':
    expression1 = "(V1 and V2)"
    var1_name1 = "V1"
    var2_name1 = "V2"
    tt1 = TruthTable(expression1, var1_name1, var2_name1)
    tt1.generate()
    tt1.display()
    print("\n" + "="*30 + "\n")
    expression2 = "(not V1 or V2)"
    var1_name2 = "V1"
    var2_name2 = "V2"
    tt2 = TruthTable(expression2, var1_name2, var2_name2)
    tt2.generate()
    tt2.display()