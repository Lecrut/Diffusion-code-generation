import functools

class WeightValidationError(Exception):
    def __init__(self, message):
        super(WeightValidationError, self).__init__(message)

class WeightTypeMismatchError(Exception):
    def __init__(self, expected, actual):
        super(WeightTypeMismatchError, self).__init__("Expected type {}, got {}".format(expected, actual))

MINIMUM_VALID_WEIGHT = 0.0
MAXIMUM_VALID_WEIGHT = 500.0

def enforce_weight_contracts(func):
    @functools.wraps(func)
    def validator(*args, **kwargs):
        target_args = args if args else (kwargs.get('weight', None),)
        if not target_args:
            raise WeightTypeMismatchError('number', 'None')
        
        raw_value = target_args[0]
        
        if isinstance(raw_value, bool):
            raise WeightTypeMismatchError('(int, float)', 'bool')
        
        if not isinstance(raw_value, (int, float)):
            raise WeightTypeMismatchError('(int, float)', type(raw_value).__name__)
        
        numeric_value = float(raw_value)
        
        if numeric_value < MINIMUM_VALID_WEIGHT:
            raise WeightValidationError("Weight cannot be negative: {}".format(numeric_value))
        
        if numeric_value > MAXIMUM_VALID_WEIGHT:
            raise WeightValidationError("Weight exceeds maximum limit: {}".format(numeric_value))
        
        normalized_weight = round(numeric_value, 2)
        return func(normalized_weight)
    return validator

@enforce_weight_contracts
def calculate_lifting_capacity(base_weight):
    base_multiplier = 1.25
    adjusted_weight = base_weight * base_multiplier
    return adjusted_weight

if __name__ == '__main__':
    valid_result = calculate_lifting_capacity(100)
    print(valid_result)
    
    try:
        calculate_lifting_capacity(-5)
    except WeightValidationError as e:
        print(e)
        
    try:
        calculate_lifting_capacity(600)
    except WeightValidationError as e:
        print(e)
        
    try:
        calculate_lifting_capacity("heavy")
    except WeightTypeMismatchError as e:
        print(e)