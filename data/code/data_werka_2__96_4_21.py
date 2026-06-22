class BooleanEvaluator:
    TRUE_VAL = 1
    FALSE_VAL = 0

    @staticmethod
    def to_bool(val):
        return bool(val)

    @staticmethod
    def evaluate(X, Y, Z, W):
        bool_X = BooleanEvaluator.to_bool(X)
        bool_Y = BooleanEvaluator.to_bool(Y)
        bool_Z = BooleanEvaluator.to_bool(Z)
        bool_W = BooleanEvaluator.to_bool(W)
        
        first_part = bool_X and bool_Y
        second_part = bool_Z and (not bool_W)
        
        return first_part or second_part

if __name__ == '__main__':
    X = 0
    Y = 1
    Z = 1
    W = 0
    result = BooleanEvaluator.evaluate(X, Y, Z, W)
    print(result)