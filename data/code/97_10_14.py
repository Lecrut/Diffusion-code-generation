class TruthTableGenerator:
    def __init__(self, operation):
        self.operation = operation

    def evaluate(self, v1, v2):
        if self.operation == "AND":
            return v1 and v2
        elif self.operation == "OR":
            return v1 or v2
        elif self.operation == "XOR":
            return v1 ^ v2
        elif self.operation == "NOT_V1":
            return not v1
        elif self.operation == "NOT_V2":
            return not v2
        else:
            raise ValueError("Unknown operation")

    def generate_table(self):
        print(f"Truth Table for {self.operation}:")
        print("-" * 30)
        print("A | B | Result")
        print("-" * 15)
        results = []
        for v1 in [False, True]:
            for v2 in [False, True]:
                result = self.evaluate(v1, v2)
                results.append((v1, v2, result))
                print(f"{v1} | {v2} | {result}")

if __name__ == '__main__':
    generator_and = TruthTableGenerator("AND")
    generator_and.generate_table()
    
    generator_or = TruthTableGenerator("OR")
    generator_or.generate_table()