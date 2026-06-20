class TruthTable:
    def __init__(self, operation):
        self.operation = operation

    def evaluate(self, var1, var2):
        if self.operation == "AND":
            return var1 and var2
        elif self.operation == "OR":
            return var1 or var2
        elif self.operation == "XOR":
            return var1 ^ var2
        elif self.operation == "NOT_V1":
            return not var1
        elif self.operation == "NOT_V2":
            return not var2
        else:
            raise ValueError("Unknown operation")

    def generate(self):
        table = []
        for v1 in [False, True]:
            for v2 in [False, True]:
                result = self.evaluate(v1, v2)
                table.append((v1, v2, result))
        return table

if __name__ == '__main__':
    tt = TruthTable("OR")
    table = tt.generate()
    print(table)