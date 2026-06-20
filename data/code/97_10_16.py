class TruthTable:
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
    NOT_V1 = "NOT_V1"
    NOT_V2 = "NOT_V2"

    def __init__(self, operation):
        self.operation = operation

    def evaluate(self, v1, v2):
        if self.operation == self.AND:
            return v1 and v2
        elif self.operation == self.OR:
            return v1 or v2
        elif self.operation == self.XOR:
            return v1 ^ v2
        elif self.operation == self.NOT_V1:
            return not v1
        elif self.operation == self.NOT_V2:
            return not v2
        else:
            raise ValueError("Unknown operation")

    def display_table(self):
        print(f"Truth Table for {self.operation}:")
        print("-" * 30)
        headers = ["A", "B", f"{self.operation}"]
        print("\t".join(headers))
        print("-" * 30)
        table_data = [
            (False, False),
            (False, True),
            (True, False),
            (True, True)
        ]
        for v1, v2 in table_data:
            result = self.evaluate(v1, v2)
            print(f"{v1}\t{v2}\t{result}")

if __name__ == '__main__':
    truth_table_and = TruthTable(TruthTable.AND)
    truth_table_or = TruthTable(TruthTable.OR)
    
    print("AND Table:")
    truth_table_and.display_table()
    print("\nOR Table:")
    truth_table_or.display_table()