class TruthTable:
    def __init__(self, expression, var1_name, var2_name, values1, values2):
        self.expression = expression
        self.var1_name = var1_name
        self.var2_name = var2_name
        self.values1 = values1
        self.values2 = values2
        self.results = []
    def evaluate(self, row):
        try:
            if self.var1_name == 'P':
                val1 = row[0]
                val2 = row[1]
            elif self.var2_name == 'Q':
                val1 = row[0]
                val2 = row[1]
            else:
                raise ValueError("Variable name not recognized.")
            if self.expression == "(P AND Q) OR P":
                result = (val1 and val2) or val1
            elif self.expression == "(P OR Q) AND R":
                pass
            elif self.expression == "P AND Q":
                result = val1 and val2
            elif self.expression == "P OR Q":
                result = val1 or val2
            elif self.expression == "NOT P":
                result = not val1
            elif self.expression == "NOT Q":
                result = not val2
            else:
                result = False
            return result
        except Exception as e:
            return f"Error during evaluation: {e}"
    def generate_table(self):
        for v1 in self.values1:
            for v2 in self.values2:
                result = self.evaluate([v1, v2])
                self.results.append((v1, v2, result))
    def display_table(self):
        header = f"{self.var1_name} | {self.var2_name} | {self.expression}\n"
        print("-" * len(header))
        for v1, v2, result in self.results:
            print(f"{v1} | {v2} | {result}")
        print("-" * len(header))
if __name__ == '__main__':
    expression1 = "P AND Q"
    var1_name1 = "P"
    var2_name1 = "Q"
    values1_1 = [0, 1]
    values2_1 = [0, 1]
    table1 = TruthTable(expression1, var1_name1, var2_name1, values1_1, values2_1)
    table1.generate_table()
    table1.display_table()
    print("\n" + "="*30 + "\n")
    expression2 = "P OR Q"
    var1_name2 = "P"
    var2_name2 = "Q"
    values1_2 = [0, 1]
    values2_2 = [0, 1]
    table2 = TruthTable(expression2, var1_name2, var2_name2, values1_2, values2_2)
    table2.generate_table()
    table2.display_table()
    print("\n" + "="*30 + "\n")
    expression3 = "NOT P"
    var1_name3 = "P"
    var2_name3 = "Q"
    values1_3 = [0, 1]
    values2_3 = [0, 1]
    table3 = TruthTable(expression3, var1_name3, var2_name3, values1_3, values2_3)
    table3.generate_table()
    table3.display_table()