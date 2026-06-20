import functools

MIN_VALID_WEIGHT = 0.0
MAX_VALID_WEIGHT = 2000.0

class WeightTypeException(TypeError):
    def __init__(self, value):
        self.value = value
        if isinstance(value, bool):
            super().__init__("Weight cannot be a boolean value.")
        else:
            super().__init__("Weight must be a numeric type (int or float), not {}.".format(type(value).__name__))

class WeightValueException(ValueError):
    def __init__(self, value):
        self.value = value
        if value < MIN_VALID_WEIGHT:
            super().__init__("Weight cannot be negative. Received: {}.".format(value))
        else:
            super().__init__("Weight exceeds maximum allowed limit of {}. Received: {}.".format(MAX_VALID_WEIGHT, value))

def normalize_weight_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise WeightTypeException("Missing required weight argument.")
        
        weight_candidate = args[0]
        
        if isinstance(weight_candidate, bool):
            raise WeightTypeException(weight_candidate)
        
        if not isinstance(weight_candidate, (int, float)):
            raise WeightTypeException(weight_candidate)
        
        if weight_candidate < MIN_VALID_WEIGHT or weight_candidate > MAX_VALID_WEIGHT:
            raise WeightValueException(weight_candidate)
        
        normalized_val = float(weight_candidate)
        new_args = (normalized_val,) + args[1:]
        return func(*new_args, **kwargs)
    return wrapper

@normalize_weight_input
def calculate_bmi(weight_kg, height_m=1.75):
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return weight_kg / (height_m ** 2)

if __name__ == '__main__':
    valid_weight = 75
    try:
        bmi_result = calculate_bmi(valid_weight)
        print(bmi_result)
    except (WeightTypeException, WeightValueException) as e:
        print(e)

    invalid_negative_weight = -10
    try:
        calculate_bmi(invalid_negative_weight)
    except (WeightTypeException, WeightValueException) as e:
        print(e)

    invalid_type_weight = "sixty"
    try:
        calculate_bmi(invalid_type_weight)
    except (WeightTypeException, WeightValueException) as e:
        print(e)
    
    invalid_bool_weight = True
    try:
        calculate_bmi(invalid_bool_weight)
    except (WeightTypeException, WeightValueException) as e:
        print(e)

    invalid_large_weight = 2500.5
    try:
        calculate_bmi(invalid_large_weight)
    except (WeightTypeException, WeightValueException) as e:
        print(e)