import functools

class WeightInputError(Exception):
    def __init__(self, message):
        super().__init__(message)

class WeightBoundsError(ValueError):
    def __init__(self, value):
        super().__init__("Weight {} is out of acceptable range".format(value))

MIN_ACCEPTABLE_WEIGHT = 1e-9
MAX_ACCEPTABLE_WEIGHT = 500.0

def ensure_positive_number(value):
    if isinstance(value, bool):
        raise WeightInputError("Boolean type is not allowed for weight")
    if not isinstance(value, (int, float)):
        raise WeightInputError("Expected numeric type, received {}".format(type(value).__name__))
    if value < MIN_ACCEPTABLE_WEIGHT:
        raise WeightBoundsError(value)
    if value > MAX_ACCEPTABLE_WEIGHT:
        raise WeightBoundsError(value)
    return float(value)

def validate_weight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) >= 1:
            raw_weight = args[0]
        elif 'weight' in kwargs:
            raw_weight = kwargs['weight']
        else:
            raise WeightInputError("Missing weight argument")
        
        normalized_weight = ensure_positive_number(raw_weight)
        
        new_args = (normalized_weight,) + args[1:]
        return func(*new_args, **kwargs)
    return wrapper

@validate_weight
def calculate_bmi_category(weight, height=1.75):
    bmi = weight / (height * height)
    if bmi < 18.5:
        return "Underweight", round(bmi, 2)
    elif bmi < 25.0:
        return "Normal", round(bmi, 2)
    elif bmi < 30.0:
        return "Overweight", round(bmi, 2)
    else:
        return "Obese", round(bmi, 2)

if __name__ == '__main__':
    try:
        result_good = calculate_bmi_category(70.5)
        print(result_good)
    except Exception as e:
        print(e)
        
    try:
        result_bad_type = calculate_bmi_category("seventy")
        print(result_bad_type)
    except Exception as e:
        print(e)
        
    try:
        result_negative = calculate_bmi_category(-10)
        print(result_negative)
    except Exception as e:
        print(e)
        
    try:
        result_too_heavy = calculate_bmi_category(600)
        print(result_too_heavy)
    except Exception as e:
        print(e)
        
    try:
        result_bool = calculate_bmi_category(True)
        print(result_bool)
    except Exception as e:
        print(e)