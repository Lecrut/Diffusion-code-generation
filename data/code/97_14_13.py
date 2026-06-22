class TruthTableGenerator:
    def __init__(self, operands, operation):
        self.operands = operands
        self.operation = operation
        self._cache = None

    def _compute_row(self, p_val, q_val):
        return {
            "x": p_val,
            "y": q_val,
            "x OR y": self.operation(p_val, q_val)
        }

    def generate(self):
        if self._cache is not None:
            return self._cache
        
        result = []
        for val1 in self.operands:
            for val2 in self.operands:
                result.append(self._compute_row(val1, val2))
        
        self._cache = result
        return result

def logical_or(a, b):
    return a or b

if __name__ == '__main__':
    inputs = [True, False]
    generator = TruthTableGenerator(inputs, logical_or)
    
    table = generator.generate()
    print(table)
    
    first_row = table[0]
    print(first_row)