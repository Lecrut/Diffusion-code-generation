class BooleanNegator:
    def __init__(self, should_negate: bool):
        self.should_negate = should_negate

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            original_result = func(*args, **kwargs)
            if self.should_negate and isinstance(original_result, bool):
                return not original_result
            return original_result
        return wrapper

def evaluate_condition(value: int) -> bool:
    return value > 10

def check_truth(val: bool) -> bool:
    return val

if __name__ == '__main__':
    negator = BooleanNegator(True)
    negated_evaluate = negator(evaluate_condition)
    negated_check = negator(check_truth)
    
    res1 = negated_evaluate(5)
    res2 = negated_evaluate(15)
    res3 = negated_check(True)
    res4 = negated_check(False)
    
    print(res1)
    print(res2)
    print(res3)
    print(res4)