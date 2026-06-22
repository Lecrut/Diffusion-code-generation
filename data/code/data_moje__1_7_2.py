import functools

class InvalidWeightTypeError(TypeError):
    def __init__(self, value):
        super().__init__("Weight must be a numeric type (int or float), not {}.".format(type(value).__name__))

class ImpossibleWeightError(ValueError):
    def __init__(self, value):
        super().__init__("Weight value {} is impossible (must be positive and <= 2000).".format(value))

MIN_WEIGHT_LIMIT = 0.0
MAX_WEIGHT_LIMIT = 2000.0

def weight_validator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise InvalidWeightTypeError("No weight argument provided")
        
        weight = args[0]
        
        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            raise InvalidWeightTypeError(weight)
        
        if weight <= MIN_WEIGHT_LIMIT or weight > MAX_WEIGHT_LIMIT:
            raise ImpossibleWeightError(weight)
        
        normalized_weight = float(weight)
        normalized_args = (normalized_weight,) + args[1:]
        
        return func(*normalized_args, **kwargs)
    return wrapper

@weight_validator
def calculate_medicine_dosage(weight_kg):
    return weight_kg * 2.5

def process_data():
    sample_cases = [
        75.5,
        100,
        -10,
        "80",
        True,
        0,
        2500
    ]
    
    for case in sample_cases:
        try:
            result = calculate_medicine_dosage(case)
            print("Input: {} -> Dosage: {}".format(case, result))
        except Exception as e:
            print("Input: {} -> Error: {}".format(case, e))

if __name__ == "__main__":
    process_data()