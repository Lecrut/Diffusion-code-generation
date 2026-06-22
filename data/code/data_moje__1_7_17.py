import functools

class WeightTypeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ImpossibleWeightError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

MIN_WEIGHT = 0.0
MAX_WEIGHT = 500.0

def _extract_weight(args, kwargs):
    weight_index = 0
    if weight_index < len(args):
        return args[weight_index]
    if 'weight' in kwargs:
        return kwargs['weight']
    raise WeightTypeError("Missing weight argument")

def _validate_type(value):
    if isinstance(value, bool):
        raise WeightTypeError("Weight cannot be a boolean value")
    if not isinstance(value, (int, float)):
        raise WeightTypeError(f"Weight must be numeric, got {type(value).__name__}")

def _validate_value(value):
    if value < MIN_WEIGHT:
        raise ImpossibleWeightError(f"Weight {value} is negative")
    if value > MAX_WEIGHT:
        raise ImpossibleWeightError(f"Weight {value} exceeds maximum limit of {MAX_WEIGHT}")

def _normalize_value(value):
    return float(value)

def validate_weight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        raw_weight = _extract_weight(args, kwargs)
        _validate_type(raw_weight)
        _validate_value(raw_weight)
        normalized_weight = _normalize_value(raw_weight)
        return func(normalized_weight)
    return wrapper

@validate_weight
def calculate_bmi(weight):
    height_m = 1.75
    return weight / (height_m * height_m)

@validate_weight
def get_weight_in_kg(weight):
    return weight

if __name__ == '__main__':
    valid_weight = 75.5
    bmi_result = calculate_bmi(valid_weight)
    print(f"BMI for {valid_weight}kg: {bmi_result:.2f}")

    kg_result = get_weight_in_kg(valid_weight)
    print(f"Weight in kg: {kg_result}")

    try:
        calculate_bmi(-10)
    except ImpossibleWeightError as e:
        print(f"Caught expected error: {e.message}")

    try:
        get_weight_in_kg("invalid")
    except WeightTypeError as e:
        print(f"Caught expected type error: {e.message}")

    try:
        calculate_bmi(True)
    except WeightTypeError as e:
        print(f"Caught expected bool error: {e.message}")