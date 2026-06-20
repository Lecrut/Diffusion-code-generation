class LogicalExpression:
    def __init__(self, operation):
        if operation not in ['AND', 'OR', 'XOR', 'NOT_V1', 'NOT_V2']:
            raise ValueError("Invalid operation")
        self.operation = operation

    def evaluate(self, v1, v2=None):
        if self.operation == 'NOT_V1':
            return not v1
        elif self.operation == 'NOT_V2':
            return not v2
        else:
            if v2 is None:
                raise ValueError("Two variables are required for AND, OR, XOR operations")
            if self.operation == 'AND':
                return v1 and v2
            elif self.operation == 'OR':
                return v1 or v2
            elif self.operation == 'XOR':
                return v1 ^ v2

def generate_truth_table(operation):
    expression = LogicalExpression(operation)
    print(f"Truth Table for {operation}:")
    print("-" * 30)
    print("A\tB\tResult")
    print("-" * 30)
    for a in [False, True]:
        for b in [False, True]:
            result = expression.evaluate(a, b) if operation != 'NOT_V1' and operation != 'NOT_V2' else expression.evaluate(a)
            print(f"{a}\t{b}\t{result}")

if __name__ == '__main__':
    generate_truth_table('AND')
    generate_truth_table('OR')
    generate_truth_table('XOR')
    generate_truth_table('NOT_V1')
    generate_truth_table('NOT_V2')