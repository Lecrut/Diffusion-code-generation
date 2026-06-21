class BooleanExpressionEvaluator:
    OP_AND = "and"
    OP_OR = "or"
    OP_NOT = "not"

    @staticmethod
    def _to_bool(value):
        return bool(value)

    @staticmethod
    def evaluate(X, Y, Z, W):
        bool_X = BooleanExpressionEvaluator._to_bool(X)
        bool_Y = BooleanExpressionEvaluator._to_bool(Y)
        bool_Z = BooleanExpressionEvaluator._to_bool(Z)
        bool_W = BooleanExpressionEvaluator._to_bool(W)

        term_left = bool_X and bool_Y
        term_right = bool_Z and (not bool_W)
        
        result = term_left or term_right
        return result

if __name__ == '__main__':
    X_val = 1
    Y_val = 0
    Z_val = 1
    W_val = 1
    evaluator = BooleanExpressionEvaluator()
    computed_result = evaluator.evaluate(X_val, Y_val, Z_val, W_val)
    print(computed_result)