class TruthTableGenerator:
    def __init__(self, operation):
        self.operation = operation

    def generate_truth_table(self):
        operations = {
            "AND": lambda v1, v2: v1 and v2,
            "OR": lambda v1, v2: v1 or v2,
            "XOR": lambda v1, v2: v1 ^ v2,
            "NOT_V1": lambda v1, v2: not v1,
            "NOT_V2": lambda v1, v2: not v2
        }
        
        if self.operation not in operations:
            return "Unknown Operation"
        
        result = []
        for v1 in [False, True]:
            for v2 in [False, True]:
                result.append((v1, v2, operations[self.operation](v1, v2)))
        
        return result

if __name__ == '__main__':
    generator = TruthTableGenerator("AND")
    print(generator.generate_truth_table())