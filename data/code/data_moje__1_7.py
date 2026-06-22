import functools

class WeightValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

class WeightDataTypeError(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_and_normalize_weight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise WeightDataTypeError("Function requires at least one argument for weight")
        weight = args[0]
        if not isinstance(weight, (int, float)):
            raise WeightDataTypeError("Weight must be a number, got {}".format(type(weight).__name__))
        if isinstance(weight, bool):
            raise WeightDataTypeError("Weight must be a number, got bool")
        if weight < 0:
            raise WeightValidationError("Weight cannot be negative")
        if weight == 0:
            raise WeightValidationError("Weight must be greater than zero")
        normalized_weight = float(weight)
        if normalized_weight > 10000:
            raise WeightValidationError("Weight exceeds maximum allowed limit of 10000")
        args = (normalized_weight,) + args[1:]
        return func(*args, **kwargs)
    return wrapper

def process_weight(weight_kg):
    return weight_kg * 2.20462

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

if __name__ == '__main__':
    result1 = process_weight(70)
    print(result1)
    
    result2 = process_weight(85.5)
    print(result2)
    
    try:
        process_weight(-5)
    except WeightValidationError as e:
        print(e)
    
    try:
        process_weight("heavy")
    except WeightDataTypeError as e:
        print(e)
    
    try:
        process_weight(0)
    except WeightValidationError as e:
        print(e)
    
    try:
        process_weight(15000)
    except WeightValidationError as e:
        print(e)
    
    try:
        process_weight(True)
    except WeightDataTypeError as e:
        print(e)
    
    bmi_result = calculate_bmi(70, 1.75)
    print(bmi_result)