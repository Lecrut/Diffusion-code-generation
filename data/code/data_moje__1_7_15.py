import functools

class InvalidWeightTypeError(TypeError):
    def __init__(self, message):
        super().__init__(message)

class ImpossibleWeightError(ValueError):
    def __init__(self, message):
        super().__init__(message)

MIN_WEIGHT_LIMIT = 0.0
MAX_WEIGHT_LIMIT = 2000.0

def validate_and_normalize_weight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) == 0:
            raise InvalidWeightTypeError("Missing weight argument")
        
        weight_input = args[0]
        
        if isinstance(weight_input, bool):
            raise InvalidWeightTypeError("Weight must be numeric, not boolean")
        
        if not isinstance(weight_input, (int, float)):
            raise InvalidWeightTypeError("Weight must be a number")
        
        normalized_weight = float(weight_input)
        
        if normalized_weight < MIN_WEIGHT_LIMIT:
            raise ImpossibleWeightError("Weight cannot be negative")
        
        if normalized_weight > MAX_WEIGHT_LIMIT:
            raise ImpossibleWeightError("Weight exceeds maximum limit")
        
        return func(normalized_weight, *args[1:], **kwargs)
    
    return wrapper

@validate_and_normalize_weight
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

if __name__ == '__main__':
    print(calculate_bmi(70, 1.75))
    print(calculate_bmi(80.5, 1.8))
    
    try:
        calculate_bmi("heavy", 1.75)
    except InvalidWeightTypeError as e:
        print(e)
    
    try:
        calculate_bmi(-5, 1.75)
    except ImpossibleWeightError as e:
        print(e)
    
    try:
        calculate_bmi(3000, 1.75)
    except ImpossibleWeightError as e:
        print(e)