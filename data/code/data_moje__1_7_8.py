import functools

class WeightTypeException(Exception):
    def __init__(self, value):
        super().__init__("Invalid type for weight: {}".format(type(value).__name__))

class WeightRangeException(Exception):
    def __init__(self, value):
        super().__init__("Invalid weight value: {}".format(value))

MAX_VALID_WEIGHT = 500.0
MIN_VALID_WEIGHT = 0.0

def ensure_valid_weight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) < 1:
            raise WeightTypeException(None)
        
        raw_value = args[0]
        
        if isinstance(raw_value, bool):
            raise WeightTypeException(raw_value)
            
        if not isinstance(raw_value, (int, float)):
            raise WeightTypeException(raw_value)
            
        if raw_value < MIN_VALID_WEIGHT or raw_value > MAX_VALID_WEIGHT:
            raise WeightRangeException(raw_value)
            
        normalized_weight = float(raw_value)
        return func(normalized_weight, *args[1:], **kwargs)
    return wrapper

@ensure_valid_weight
def compute_mass_kg(weight):
    return weight

@ensure_valid_weight
def convert_to_pounds(weight):
    conversion_factor = 2.20462
    return weight * conversion_factor

if __name__ == '__main__':
    test_valid = 75.5
    test_invalid_type = "75"
    test_negative = -10
    test_too_heavy = 1000
    
    print(compute_mass_kg(test_valid))
    print(convert_to_pounds(test_valid))
    
    try:
        compute_mass_kg(test_invalid_type)
    except WeightTypeException as e:
        print(e)
        
    try:
        compute_mass_kg(test_negative)
    except WeightRangeException as e:
        print(e)
        
    try:
        compute_mass_kg(test_too_heavy)
    except WeightRangeException as e:
        print(e)