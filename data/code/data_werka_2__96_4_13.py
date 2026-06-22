TRUE_VALUE = 1
FALSE_VALUE = 0

def evaluate_logic_expression(X, Y, Z, W):
    bool_X = bool(X)
    bool_Y = bool(Y)
    bool_Z = bool(Z)
    bool_W = bool(W)
    
    term_one = bool_X and bool_Y
    term_two = bool_Z and (not bool_W)
    
    return term_one or term_two

class LogicEvaluator:
    def __init__(self, X, Y, Z, W):
        self.X = bool(X)
        self.Y = bool(Y)
        self.Z = bool(Z)
        self.W = bool(W)
    
    def compute(self):
        part_a = self.X and self.Y
        part_b = self.Z and (not self.W)
        return part_a or part_b

if __name__ == '__main__':
    sample_X = 1
    sample_Y = 0
    sample_Z = 1
    sample_W = 0
    
    evaluator = LogicEvaluator(sample_X, sample_Y, sample_Z, sample_W)
    result = evaluator.compute()
    print(result)