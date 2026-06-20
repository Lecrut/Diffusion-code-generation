import functools

class InvalidWeightTypeError(TypeError):
    def __init__(self, value):
        message = "Weight must be a numeric type, not {}.".format(type(value).__name__)
        super().__init__(message)

class ImpossibleWeightError(ValueError):
    def __init__(self, value):
        message = "Weight value {} is impossible; must be non-negative and less than 5000.".format(value)
        super().__init__(message)

MIN_WEIGHT = 0.0
MAX_WEIGHT = 5000.0

def normalize_weight_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        weight_arg = None
        if args:
            weight_arg = args[0]
        elif 'weight' in kwargs:
            weight_arg = kwargs['weight']
        else:
            raise InvalidWeightTypeError("None")
        
        if isinstance(weight_arg, bool):
            raise InvalidWeightTypeError(weight_arg)
        
        if not isinstance(weight_arg, (int, float)):
            raise InvalidWeightTypeError(weight_arg)
        
        if weight_arg < MIN_WEIGHT or weight_arg >= MAX_WEIGHT:
            raise ImpossibleWeightError(weight_arg)
        
        normalized_value = float(weight_arg)
        return func(normalized_value)
    return wrapper

@normalize_weight_input
def calculate_bmi_scale_factor(weight):
    base_factor = 0.453592
    return weight * base_factor

if __name__ == '__main__':
    test_cases = [150, 0, 5001, -5, "invalid", True, 250.5]
    for val in test_cases:
        try:
            result = calculate_bmi_scale_factor(val)
            print("Input: {} -> Result: {}".format(val, result))
        except (InvalidWeightTypeError, ImpossibleWeightError) as e:
            print("Input: {} -> Error: {}".format(val, str(e)))