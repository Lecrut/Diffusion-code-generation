class BooleanOperations:
    def __init__(self):
        self.operations = {
            'AND': lambda a, b: a and b,
            'OR': lambda a, b: a or b,
            'NOT': lambda a: not a,
            'XOR': lambda a, b: a != b,
            'NAND': lambda a, b: not (a and b),
            'NOR': lambda a, b: not (a or b),
            'IMPLIES': lambda a, b: not a or b
        }

    def get_results(self):
        return self.operations

if __name__ == '__main__':
    boolean_ops = BooleanOperations()
    results = boolean_ops.get_results()
    print(results)