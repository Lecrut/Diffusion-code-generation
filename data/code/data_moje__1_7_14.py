import functools

INVALID_WEIGHT_TYPE_MSG = "Weight must be a numeric type (int or float), not {}."
IMPOSSIBLE_WEIGHT_MSG = "Weight value {} is impossible (must be 0.0 to 500.0)."
MIN_VALID_WEIGHT = 0.0
MAX_VALID_WEIGHT = 500.0

class WeightTypeError(TypeError):
    def __init__(self, value):
        if isinstance(value, type):
            super().__init__(INVALID_WEIGHT_TYPE_MSG.format(value.__name__))
        else:
            super().__init__(INVALID_WEIGHT_TYPE_MSG.format(type(value).__name__))

class ImpossibleWeightError(ValueError):
    def __init__(self, value):
        super().__init__(IMPOSSIBLE_WEIGHT_MSG.format(value))

def normalize_weight_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise WeightTypeError(type(None))
        
        raw_weight = args[0]
        
        if isinstance(raw_weight, bool):
            raise WeightTypeError(raw_weight)
        
        if not isinstance(raw_weight, (int, float)):
            raise WeightTypeError(raw_weight)
        
        if raw_weight < MIN_VALID_WEIGHT or raw_weight > MAX_VALID_WEIGHT:
            raise ImpossibleWeightError(raw_weight)
        
        normalized_value = float(raw_weight)
        return func(normalized_value)
    
    return wrapper

@normalize_weight_decorator
def calculate_bmi(weight):
    height = 1.75
    return weight / (height ** 2)

if __name__ == '__main__':
    test_values = [75.5, 0, 500, "invalid", True, -10, 600]
    
    for value in test_values:
        try:
            result = calculate_bmi(value)
            print("Input: {}, Result: {:.2f}".format(value, result))
        except (WeightTypeError, ImpossibleWeightError) as e:
            print("Input: {}, Error: {}".format(repr(value), str(e)))