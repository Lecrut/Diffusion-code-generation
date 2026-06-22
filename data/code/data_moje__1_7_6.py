import functools

MIN_WEIGHT = 0.0
MAX_WEIGHT = 500.0

class WeightDataTypeError(Exception):
    def __init__(self, value):
        msg = "Invalid weight type: expected number, got {}".format(type(value).__name__)
        super().__init__(msg)

class WeightValueError(Exception):
    def __init__(self, value):
        msg = "Impossible weight value: {} must be between {} and {}".format(value, MIN_WEIGHT, MAX_WEIGHT)
        super().__init__(msg)

def normalize_weight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise WeightDataTypeError("No weight argument provided")
        raw_weight = args[0]
        
        if isinstance(raw_weight, bool):
            raise WeightDataTypeError(raw_weight)
        
        if not isinstance(raw_weight, (int, float)):
            raise WeightDataTypeError(raw_weight)
        
        if raw_weight < MIN_WEIGHT or raw_weight > MAX_WEIGHT:
            raise WeightValueError(raw_weight)
        
        normalized = round(float(raw_weight), 4)
        return func(normalized)
    return wrapper

@normalize_weight
def calculate_bmi_scale(weight):
    return weight * 2.54

if __name__ == '__main__':
    try:
        result = calculate_bmi_scale(70)
        print(result)
    except (WeightDataTypeError, WeightValueError) as e:
        print(e)

    try:
        invalid_result = calculate_bmi_scale(-5)
        print(invalid_result)
    except (WeightDataTypeError, WeightValueError) as e:
        print(e)

    try:
        type_result = calculate_bmi_scale("100")
        print(type_result)
    except (WeightDataTypeError, WeightValueError) as e:
        print(e)